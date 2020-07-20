import os
import random

from nonebot.exceptions import CQHttpError

from hoshino import R, Service, priv
from hoshino.util import FreqLimiter, DailyNumberLimiter
from hoshino.config.mantra import KEYWORD

_max = 50
EXCEED_NOTICE = f'您今天已经迫害过艹爷{_max}次了，欢迎明早5点后再来迫害！'
_n_limit = DailyNumberLimiter(_max)
_f_limit = FreqLimiter(5)

sv = Service('mantra', manage_priv=priv.SUPERUSER, enable_on_default=True, visible=False)
mantra_folder = R.img('mantra/').path


def mantra_generator():
    while True:
        file_list = os.listdir(mantra_folder)
        random.shuffle(file_list)
        for filename in file_list:
            if os.path.isfile(os.path.join(mantra_folder, filename)):
                yield R.img('mantra/', filename)


mantra_generator = mantra_generator()


def get_mantra():
    return mantra_generator.__next__()


@sv.on_rex(KEYWORD)
async def setu(bot, ev):
    """随机叫一份真言语录，对每个用户有冷却时间"""
    uid = ev['user_id']
    if not _n_limit.check(uid):
        await bot.send(ev, EXCEED_NOTICE, at_sender=True)
        return
    if not _f_limit.check(uid):
        await bot.send(ev, '您迫害的太频繁了，请稍候再迫害', at_sender=True)
        return
    _f_limit.start_cd(uid)
    _n_limit.increase(uid)

    # conditions all ok, send a setu.
    pic = get_mantra()
    try:
        await bot.send(ev, pic.cqcode)
    except CQHttpError:
        sv.logger.error(f"发送图片{pic.path}失败")
        try:
            await bot.send(ev, '太艹了，发不出去勒...')
        except:
            pass
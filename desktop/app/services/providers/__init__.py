# coding: utf-8
from .aiting import AitingProvider
from .base import MusicProvider
from .bodian import BodianProvider
from .bugu import BuguProvider
from .gequbao import GequbaoProvider
from .gequhai import GequhaiProvider
from .jianbin import JianbinProvider
from .joox import JooxProvider
from .kugou import KugouProvider
from .livepoo import LivepooProvider
from .migu import MiguProvider
from .netease_official import NeteaseOfficialProvider
from .qq import QQProvider
from .qq_official import QQOfficialProvider
from .qqmp3 import QQMp3Provider

PROVIDERS: dict[str, MusicProvider] = {
    "netease": NeteaseOfficialProvider(),
    "qq-official": QQOfficialProvider(),
    "kugou": KugouProvider(),
    "gequbao": GequbaoProvider(),
    "gequhai": GequhaiProvider(),
    "bugu": BuguProvider(),
    "bodian": BodianProvider(),
    "qq": QQProvider(),
    "qqmp3": QQMp3Provider(),
    "mitu": QQMp3Provider("mitu"),
    "joox": JooxProvider(),
    "migu": MiguProvider(),
    "livepoo": LivepooProvider(),
    "aiting": AitingProvider(),
    "jianbin-netease": JianbinProvider("jianbin-netease", "netease"),
    "jianbin-qq": JianbinProvider("jianbin-qq", "qq"),
    "jianbin-kugou": JianbinProvider("jianbin-kugou", "kugou"),
    "jianbin-kuwo": JianbinProvider("jianbin-kuwo", "kuwo"),
}

PROVIDER_DISPLAY_NAMES = {
    "cenguigui": "netease",
    "XCVTS": "qq-official",
    "海棠": "kugou",
    "歌曲宝": "gequbao",
    "歌曲海": "gequhai",
    "布谷": "bugu",
    "波点": "bodian",
    "QQMP3": "qqmp3",
    "米兔": "mitu",
    "JOOX": "joox",
    "咪咕": "migu",
    "力音": "livepoo",
    "爱听": "aiting",
    "煎饼-1": "jianbin-netease",
    "煎饼-2": "jianbin-qq",
    "煎饼-3": "jianbin-kugou",
    "煎饼-4": "jianbin-kuwo",
}


def get_provider(name: str = "netease") -> MusicProvider:
    provider_key = PROVIDER_DISPLAY_NAMES.get(name, name)
    return PROVIDERS.get(provider_key) or PROVIDERS["netease"]


def get_all_providers() -> list[MusicProvider]:
    return list(PROVIDERS.values())


__all__ = [
    "MusicProvider",
    "PROVIDER_DISPLAY_NAMES",
    "get_all_providers",
    "get_provider",
]

from enum import IntEnum


class CardSet(IntEnum):
	"""TAG_CARD_SET"""

	INVALID = 0
	TEST_TEMPORARY = 1
	BASIC = 2
	EXPERT1 = 3
	HOF = 4
	MISSIONS = 5
	DEMO = 6
	NONE = 7
	CHEAT = 8
	BLANK = 9
	DEBUG_SP = 10
	PROMO = 11
	NAXX = 12  # Curse of Naxxramas
	GVG = 13  # Goblins vs Gnomes
	BRM = 14  # Blackrock Mountain
	TGT = 15  # The Grand Tournament
	CREDITS = 16
	HERO_SKINS = 17
	TB = 18  # Tavern Brawl
	SLUSH = 19
	LOE = 20  # The League of Explorers
	OG = 21  # Whispers of the Old Gods
	OG_RESERVE = 22
	KARA = 23  # One Night in Karazhan
	KARA_RESERVE = 24
	GANGS = 25  # Mean Streets of Gadgetzan
	GANGS_RESERVE = 26
	UNGORO = 27  # Journey to Un'Goro
	ICECROWN = 1001  # Knights of the Frozen Throne
	LOOTAPALOOZA = 1004  # Kobolds & Catacombs
	GILNEAS = 1125  # The Witchwood
	BOOMSDAY = 1127  # The Boomsday Project
	TROLL = 1129  # Rastakhan's Rumble
	DALARAN = 1130  # Rise of Shadows
	ULDUM = 1158  # Saviours of Uldum
	DRAGONS = 1347  # Descent of Dragons
	YEAR_OF_THE_DRAGON = 1403
	BLACK_TEMPLE = 1414  # Ashes of Outlands
	WILD_EVENT = 1439
	SCHOLOMANCE = 1443  # Scholomance Academy
	BATTLEGROUNDS = 1453
	DEMON_HUNTER_INITIATE = 1463
	DARKMOON_FAIRE = 1466  # Madness at the Darkmoon Faire
	THE_BARRENS = 1525  # Forged in the Barrens
	WAILING_CAVERNS = 1559
	STORMWIND = 1578  # United in Stormwind
	LETTUCE = 1586  # Mercenaries
	ALTERAC_VALLEY = 1626  # Fractured in Alterac Valley
	LEGACY = 1635
	CORE = 1637
	VANILLA = 1646
	THE_SUNKEN_CITY = 1658  # Voyage to the Sunken City
	REVENDRETH = 1691  # Murder at Castle Nathria
	MERCENARIES_DEV = 1705
	RETURN_OF_THE_LICH_KING = 1776
	BATTLE_OF_THE_BANDS = 1809
	TITANS = 1858
	PATH_OF_ARTHAS = 1869
	WILD_WEST = 1892
	WONDERS = 1898

	# Not actually present...
	TAVERNS_OF_TIME = 1143
	PLACEHOLDER_202204 = 1810

	# Aliased from the original enums
	FP1 = 12
	PE1 = 13


class CardType(IntEnum):
	"""TAG_CARDTYPE"""

	INVALID = 0
	GAME = 1
	PLAYER = 2
	HERO = 3
	MINION = 4
	SPELL = 5
	ENCHANTMENT = 6
	WEAPON = 7
	ITEM = 8
	TOKEN = 9
	HERO_POWER = 10
	BLANK = 11
	GAME_MODE_BUTTON = 12
	MOVE_MINION_HOVER_TARGET = 22
	LETTUCE_ABILITY = 23
	BATTLEGROUND_HERO_BUDDY = 24
	LOCATION = 39
	BATTLEGROUND_QUEST_REWARD = 40
	BATTLEGROUND_ANOMALY = 43


class Rarity(IntEnum):
	"""TAG_RARITY"""

	INVALID = 0
	COMMON = 1
	FREE = 2
	RARE = 3
	EPIC = 4
	LEGENDARY = 5


class CardClass(IntEnum):
	"""TAG_CLASS"""

	INVALID = 0
	DEATHKNIGHT = 1
	DRUID = 2
	HUNTER = 3
	MAGE = 4
	PALADIN = 5
	PRIEST = 6
	ROGUE = 7
	SHAMAN = 8
	WARLOCK = 9
	WARRIOR = 10
	DREAM = 11
	NEUTRAL = 12
	WHIZBANG = 13
	DEMONHUNTER = 14


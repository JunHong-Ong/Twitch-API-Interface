import unittest

from twitch.models import (
    Badge, ChannelBadge,
    Channel,
    Cheermote, CheermoteTier,
    Clip,
    Emote, ChannelEmote, EmoteSet,
    Game,
    User,
    Video
)

class TestModels(unittest.TestCase):
    """Test cases for various models created"""

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_channel_badge(self):
        CHANNEL_CHAT_BADGES = [
            {
                "set_id": "bits",
                "versions": [
                    {
                        "id": "1",
                        "image_url_1x": "https://static-cdn.jtvnw.net/badges/v1/743a0f3b-84b3-450b-96a0-503d7f4a9764/1",
                        "image_url_2x": "https://static-cdn.jtvnw.net/badges/v1/743a0f3b-84b3-450b-96a0-503d7f4a9764/2",
                        "image_url_4x": "https://static-cdn.jtvnw.net/badges/v1/743a0f3b-84b3-450b-96a0-503d7f4a9764/3"
                    }
                ]
            },
            {
                "set_id": "subscriber",
                "versions": [
                    {
                        "id": "0",
                        "image_url_1x": "https://static-cdn.jtvnw.net/badges/v1/eb4a8a4c-eacd-4f5e-b9f2-394348310442/1",
                        "image_url_2x": "https://static-cdn.jtvnw.net/badges/v1/eb4a8a4c-eacd-4f5e-b9f2-394348310442/2",
                        "image_url_4x": "https://static-cdn.jtvnw.net/badges/v1/eb4a8a4c-eacd-4f5e-b9f2-394348310442/3"
                    }
                ]
            }
        ]

        channel_badge = ChannelBadge(CHANNEL_CHAT_BADGES[0])
        self.assertIsNotNone(channel_badge)
        self.assertIsInstance(channel_badge, ChannelBadge)
        self.assertEqual(channel_badge.set_id, CHANNEL_CHAT_BADGES[0].get("set_id"))
        self.assertEqual(channel_badge.versions, CHANNEL_CHAT_BADGES[0].get("versions"))


    def test_create_global_badge(self):
        GLOBAL_CHAT_BADGE = [
            {
                "set_id": "vip",
                "versions": [
                    {
                        "id": "1",
                        "image_url_1x": "https://static-cdn.jtvnw.net/badges/v1/b817aba4-fad8-49e2-b88a-7cc744dfa6ec/1",
                        "image_url_2x": "https://static-cdn.jtvnw.net/badges/v1/b817aba4-fad8-49e2-b88a-7cc744dfa6ec/2",
                        "image_url_4x": "https://static-cdn.jtvnw.net/badges/v1/b817aba4-fad8-49e2-b88a-7cc744dfa6ec/3"
                    }
                ]
            }
        ]

        global_badge = Badge(GLOBAL_CHAT_BADGE[0])
        self.assertIsNotNone(global_badge)
        self.assertIsInstance(global_badge, Badge)
        self.assertEqual(global_badge.set_id, GLOBAL_CHAT_BADGE[0].get("set_id"))
        self.assertEqual(global_badge.versions, GLOBAL_CHAT_BADGE[0].get("versions"))


    def test_create_channel(self):
        CHANNEL_DATA = [
            {
                "broadcaster_id": "141981764",
                "broadcaster_login": "twitchdev",
                "broadcaster_name": "TwitchDev",
                "broadcaster_language": "en",
                "game_id": "509670",
                "game_name": "Science & Technology",
                "title": "TwitchDev Monthly Update // May 6, 2021",
                "delay": 0,
                "tags": ["DevsInTheKnow"]
            }
        ]

        channel = Channel(CHANNEL_DATA[0])
        self.assertIsNotNone(channel)
        self.assertIsInstance(channel, Channel)
        self.assertEqual(channel.broadcaster_id, CHANNEL_DATA[0].get("broadcaster_id"))
        self.assertEqual(channel.broadcaster_login, CHANNEL_DATA[0].get("broadcaster_login"))
        self.assertEqual(channel.broadcaster_name, CHANNEL_DATA[0].get("broadcaster_name"))
        self.assertEqual(channel.broadcaster_language, CHANNEL_DATA[0].get("broadcaster_language"))
        self.assertEqual(channel.game_name, CHANNEL_DATA[0].get("game_name"))
        self.assertEqual(channel.game_id, CHANNEL_DATA[0].get("game_id"))
        self.assertEqual(channel.title, CHANNEL_DATA[0].get("title"))
        self.assertEqual(channel.delay, CHANNEL_DATA[0].get("delay"))
        self.assertEqual(channel.tags, CHANNEL_DATA[0].get("tags"))


    def test_create_cheermote(self):
        CHEERMOTE_DATA = [
            {
                "prefix": "Cheer",
                "tiers": [
                    {
                    "min_bits": 1,
                    "id": "1",
                    "color": "#979797",
                    "images": {
                        "dark": {
                        "animated": {
                            "1": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/animated/1/1.gif",
                            "1.5": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/animated/1/1.5.gif",
                            "2": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/animated/1/2.gif",
                            "3": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/animated/1/3.gif",
                            "4": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/animated/1/4.gif"
                        },
                        "static": {
                            "1": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/static/1/1.png",
                            "1.5": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/static/1/1.5.png",
                            "2": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/static/1/2.png",
                            "3": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/static/1/3.png",
                            "4": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/static/1/4.png"
                        }
                        },
                        "light": {
                        "animated": {
                            "1": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/animated/1/1.gif",
                            "1.5": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/animated/1/1.5.gif",
                            "2": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/animated/1/2.gif",
                            "3": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/animated/1/3.gif",
                            "4": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/animated/1/4.gif"
                        },
                        "static": {
                            "1": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/static/1/1.png",
                            "1.5": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/static/1/1.5.png",
                            "2": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/static/1/2.png",
                            "3": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/static/1/3.png",
                            "4": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/static/1/4.png"
                        }
                        }
                    },
                    "can_cheer": True,
                    "show_in_bits_card": True
                    }
                ],
                "type": "global_first_party",
                "order": 1,
                "last_updated": "2018-05-22T00:06:04Z",
                "is_charitable": False
            }
        ]

        cheermote = Cheermote(CHEERMOTE_DATA[0])
        self.assertIsNotNone(Cheermote)
        self.assertIsInstance(cheermote, Cheermote)
        self.assertEqual(cheermote.prefix, CHEERMOTE_DATA[0].get("prefix"))
        for index, cheermote_tier in enumerate(cheermote.tiers):
            self.assertIsInstance(cheermote_tier, CheermoteTier)
            self.assertEqual(cheermote_tier.min_bits, CHEERMOTE_DATA[0]["tiers"][index]["min_bits"])
            self.assertEqual(cheermote_tier.id, CHEERMOTE_DATA[0]["tiers"][index]["id"])
            self.assertEqual(cheermote_tier.color, CHEERMOTE_DATA[0]["tiers"][index]["color"])
            self.assertEqual(cheermote_tier.images, CHEERMOTE_DATA[0]["tiers"][index]["images"])
            self.assertEqual(cheermote_tier.can_cheer, CHEERMOTE_DATA[0]["tiers"][index]["can_cheer"])
            self.assertEqual(cheermote_tier.show_in_bits_card, CHEERMOTE_DATA[0]["tiers"][index]["show_in_bits_card"])
        self.assertEqual(cheermote.type, CHEERMOTE_DATA[0].get("type"))
        self.assertEqual(cheermote.order, CHEERMOTE_DATA[0].get("order"))
        self.assertEqual(cheermote.last_updated, CHEERMOTE_DATA[0].get("last_updated"))
        self.assertEqual(cheermote.is_charitable, CHEERMOTE_DATA[0].get("is_charitable"))


    def test_create_clip(self):
        CLIP_DATA = [
            {
                "id": "AwkwardHelplessSalamanderSwiftRage",
                "url": "https://clips.twitch.tv/AwkwardHelplessSalamanderSwiftRage",
                "embed_url": "https://clips.twitch.tv/embed?clip=AwkwardHelplessSalamanderSwiftRage",
                "broadcaster_id": "67955580",
                "broadcaster_name": "ChewieMelodies",
                "creator_id": "53834192",
                "creator_name": "BlackNova03",
                "video_id": "205586603",
                "game_id": "488191",
                "language": "en",
                "title": "babymetal",
                "view_count": 10,
                "created_at": "2017-11-30T22:34:18Z",
                "thumbnail_url": "https://clips-media-assets.twitch.tv/157589949-preview-480x272.jpg",
                "duration": 60,
                "vod_offset": 480
            }
        ]

        clip = Clip(CLIP_DATA[0])
        self.assertIsNotNone(clip)
        self.assertIsInstance(clip, Clip)
        self.assertEqual(clip.id, CLIP_DATA[0]["id"])
        self.assertEqual(clip.url, CLIP_DATA[0]["url"])
        self.assertEqual(clip.embed_url, CLIP_DATA[0]["embed_url"])
        self.assertEqual(clip.broadcaster_id, CLIP_DATA[0]["broadcaster_id"])
        self.assertEqual(clip.broadcaster_name, CLIP_DATA[0]["broadcaster_name"])
        self.assertEqual(clip.creator_id, CLIP_DATA[0]["creator_id"])
        self.assertEqual(clip.creator_name, CLIP_DATA[0]["creator_name"])
        self.assertEqual(clip.video_id, CLIP_DATA[0]["video_id"])
        self.assertEqual(clip.game_id, CLIP_DATA[0]["game_id"])
        self.assertEqual(clip.language, CLIP_DATA[0]["language"])
        self.assertEqual(clip.title, CLIP_DATA[0]["title"])
        self.assertEqual(clip.view_count, CLIP_DATA[0]["view_count"])
        self.assertEqual(clip.created_at, CLIP_DATA[0]["created_at"])
        self.assertEqual(clip.thumbnail_url, CLIP_DATA[0]["thumbnail_url"])
        self.assertEqual(clip.duration, CLIP_DATA[0]["duration"])
        self.assertEqual(clip.vod_offset, CLIP_DATA[0]["vod_offset"])


    def test_create_emote(self):
        EMOTE_DATA =   [
            {
                "id": "196892",
                "name": "TwitchUnity",
                "images": {
                    "url_1x": "https://static-cdn.jtvnw.net/emoticons/v2/196892/static/light/1.0",
                    "url_2x": "https://static-cdn.jtvnw.net/emoticons/v2/196892/static/light/2.0",
                    "url_4x": "https://static-cdn.jtvnw.net/emoticons/v2/196892/static/light/3.0"
                },
                "format": [
                    "static"
                ],
                "scale": [
                    "1.0",
                    "2.0",
                    "3.0"
                ],
                "theme_mode": [
                    "light",
                    "dark"
                ]
            }
        ]

        emote = Emote(EMOTE_DATA[0])
        self.assertIsNotNone(emote)
        self.assertIsInstance(emote, Emote)
        self.assertEqual(emote.id, EMOTE_DATA[0]["id"])
        self.assertEqual(emote.name, EMOTE_DATA[0]["name"])
        self.assertEqual(emote.images, EMOTE_DATA[0]["images"])
        self.assertEqual(emote.format, EMOTE_DATA[0]["format"])
        self.assertEqual(emote.scale, EMOTE_DATA[0]["scale"])
        self.assertEqual(emote.theme_mode, EMOTE_DATA[0]["theme_mode"])


    def test_create_emote_set(self):
        EMOTE_SET_DATA = [
            {
                "id": "304456832",
                "name": "twitchdevPitchfork",
                "images": {
                    "url_1x": "https://static-cdn.jtvnw.net/emoticons/v2/304456832/static/light/1.0",
                    "url_2x": "https://static-cdn.jtvnw.net/emoticons/v2/304456832/static/light/2.0",
                    "url_4x": "https://static-cdn.jtvnw.net/emoticons/v2/304456832/static/light/3.0"
                },
                "emote_type": "subscriptions",
                "emote_set_id": "301590448",
                "owner_id": "141981764",
                "format": [
                    "static"
                ],
                "scale": [
                    "1.0",
                    "2.0",
                    "3.0"
                ],
                "theme_mode": [
                    "light",
                    "dark"
                ]
            }
        ]
    
        emote_set = EmoteSet(EMOTE_SET_DATA)
        self.assertIsNotNone(emote_set)
        self.assertIsInstance(emote_set, EmoteSet)
        for emote in emote_set.emotes:
            self.assertIsNotNone(emote)
            self.assertIsInstance(emote, ChannelEmote)


    def test_create_channel_emote(self):
        CHANNEL_EMOTE_DATA = [
            {
            "id": "304456832",
            "name": "twitchdevPitchfork",
            "images": {
                "url_1x": "https://static-cdn.jtvnw.net/emoticons/v2/304456832/static/light/1.0",
                "url_2x": "https://static-cdn.jtvnw.net/emoticons/v2/304456832/static/light/2.0",
                "url_4x": "https://static-cdn.jtvnw.net/emoticons/v2/304456832/static/light/3.0"
            },
            "tier": "1000",
            "emote_type": "subscriptions",
            "emote_set_id": "301590448",
            "format": [
                "static"
            ],
            "scale": [
                "1.0",
                "2.0",
                "3.0"
            ],
            "theme_mode": [
                "light",
                "dark"
            ]
            },
            {
            "id": "emotesv2_4c3b4ed516de493bbcd2df2f5d450f49",
            "name": "twitchdevHyperPitchfork",
            "images": {
                "url_1x": "https://static-cdn.jtvnw.net/emoticons/v2/emotesv2_4c3b4ed516de493bbcd2df2f5d450f49/static/light/1.0",
                "url_2x": "https://static-cdn.jtvnw.net/emoticons/v2/emotesv2_4c3b4ed516de493bbcd2df2f5d450f49/static/light/2.0",
                "url_4x": "https://static-cdn.jtvnw.net/emoticons/v2/emotesv2_4c3b4ed516de493bbcd2df2f5d450f49/static/light/3.0"
            },
            "tier": "1000",
            "emote_type": "subscriptions",
            "emote_set_id": "318939165",
            "format": [
                "static",
                "animated"
            ],
            "scale": [
                "1.0",
                "2.0",
                "3.0"
            ],
            "theme_mode": [
                "light",
                "dark"
            ]
            }
        ]

        channel_emote = ChannelEmote(CHANNEL_EMOTE_DATA[0])
        self.assertIsNotNone(channel_emote)
        self.assertIsInstance(channel_emote, ChannelEmote)
        self.assertEqual(channel_emote.tier, CHANNEL_EMOTE_DATA[0]["tier"])
        self.assertEqual(channel_emote.emote_type, CHANNEL_EMOTE_DATA[0]["emote_type"])
        self.assertEqual(channel_emote.emote_set_id, CHANNEL_EMOTE_DATA[0]["emote_set_id"])
        self.assertEqual(channel_emote.owner_id, None)


    def test_create_game(self):
        GAME_DATA = [
            {
                "id": "33214",
                "name": "Fortnite",
                "box_art_url": "https://static-cdn.jtvnw.net/ttv-boxart/33214-{width}x{height}.jpg",
                "igdb_id": "1905"
            }
        ]

        game = Game(GAME_DATA[0])
        self.assertIsNotNone(game)
        self.assertIsInstance(game, Game)
        self.assertEqual(game.id, GAME_DATA[0]["id"])
        self.assertEqual(game.name, GAME_DATA[0]["name"])
        self.assertEqual(game.box_art_url, GAME_DATA[0]["box_art_url"])
        self.assertEqual(game.igdb_id, GAME_DATA[0]["igdb_id"])


    def test_create_user(self):
        USER_DATA = [
            {
                "id": "141981764",
                "login": "twitchdev",
                "display_name": "TwitchDev",
                "type": "",
                "broadcaster_type": "partner",
                "description": "Supporting third-party developers building Twitch integrations from chatbots to game integrations.",
                "profile_image_url": "https://static-cdn.jtvnw.net/jtv_user_pictures/8a6381c7-d0c0-4576-b179-38bd5ce1d6af-profile_image-300x300.png",
                "offline_image_url": "https://static-cdn.jtvnw.net/jtv_user_pictures/3f13ab61-ec78-4fe6-8481-8682cb3b0ac2-channel_offline_image-1920x1080.png",
                "view_count": 5980557,
                "email": "not-real@email.com",
                "created_at": "2016-12-14T20:32:28Z"
            }
        ]

        user = User(USER_DATA[0])
        self.assertIsNotNone(user)
        self.assertIsInstance(user, User)
        self.assertEqual(user.id, USER_DATA[0]["id"])
        self.assertEqual(user.login, USER_DATA[0]["login"])
        self.assertEqual(user.display_name, USER_DATA[0]["display_name"])
        self.assertEqual(user.type, USER_DATA[0]["type"])
        self.assertEqual(user.broadcaster_type, USER_DATA[0]["broadcaster_type"])
        self.assertEqual(user.description, USER_DATA[0]["description"])
        self.assertEqual(user.profile_image_url, USER_DATA[0]["profile_image_url"])
        self.assertEqual(user.offline_image_url, USER_DATA[0]["offline_image_url"])
        self.assertEqual(user.created_at, USER_DATA[0]["created_at"])


    def test_create_video(self):
        VIDEO_DATA = [
            {
                "id": "335921245",
                "stream_id": None,
                "user_id": "141981764",
                "user_login": "twitchdev",
                "user_name": "TwitchDev",
                "title": "Twitch Developers 101",
                "description": "Welcome to Twitch development! Here is a quick overview of our products and information to help you get started.",
                "created_at": "2018-11-14T21:30:18Z",
                "published_at": "2018-11-14T22:04:30Z",
                "url": "https://www.twitch.tv/videos/335921245",
                "thumbnail_url": "https://static-cdn.jtvnw.net/cf_vods/d2nvs31859zcd8/twitchdev/335921245/ce0f3a7f-57a3-4152-bc06-0c6610189fb3/thumb/index-0000000000-%{width}x%{height}.jpg",
                "viewable": "public",
                "view_count": 1863062,
                "language": "en",
                "type": "upload",
                "duration": "3m21s",
                "muted_segments": [
                    {
                        "duration": 30,
                        "offset": 120
                    }
                ]
            }
        ]

        video = Video(VIDEO_DATA[0])
        self.assertIsNotNone(video)
        self.assertIsInstance(video, Video)
        self.assertEqual(video.id, VIDEO_DATA[0]["id"])
        self.assertEqual(video.stream_id, VIDEO_DATA[0]["stream_id"])
        self.assertEqual(video.user_id, VIDEO_DATA[0]["user_id"])
        self.assertEqual(video.user_login, VIDEO_DATA[0]["user_login"])
        self.assertEqual(video.user_name, VIDEO_DATA[0]["user_name"])
        self.assertEqual(video.title, VIDEO_DATA[0]["title"])
        self.assertEqual(video.description, VIDEO_DATA[0]["description"])
        self.assertEqual(video.created_at, VIDEO_DATA[0]["created_at"])
        self.assertEqual(video.published_at, VIDEO_DATA[0]["published_at"])
        self.assertEqual(video.url, VIDEO_DATA[0]["url"])
        self.assertEqual(video.thumbnail_url, VIDEO_DATA[0]["thumbnail_url"])
        self.assertEqual(video.viewable, VIDEO_DATA[0]["viewable"])
        self.assertEqual(video.view_count, VIDEO_DATA[0]["view_count"])
        self.assertEqual(video.language, VIDEO_DATA[0]["language"])
        self.assertEqual(video.type, VIDEO_DATA[0]["type"])
        self.assertEqual(video.duration, VIDEO_DATA[0]["duration"])
        self.assertEqual(video.muted_segments, VIDEO_DATA[0]["muted_segments"])

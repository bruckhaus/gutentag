import random
import unittest
from ..tagger import Tagger


class TestTagger(unittest.TestCase):

    def test_tag(self):

        text = """The Buddha, the Godhead, resides quite as comfortably in the circuits of a digital
        computer or the gears of a cycle transmission as he does at the top of a mountain
        or in the petals of a flower. To think otherwise is to demean the Buddha...which is
        to demean oneself."""

        self.assertTrue(Tagger.tag(text) == 'foo')

        #text = """Marketaire.com  Founder - Internet marketing strategies & tactics. SEO, SEM, SMM. Let's do this.
        #Toronto, Ontario, Canada . marketaire.com"""
        #
        #text = """SEM SEO SMM PPC Performance Suchmaschinen Marketing sponsored listings affiliate adwords paid
        #search social ROI tracking; twitterbot; follow @ressmann my human"""
        #
        #text = """#Technology, science, self-development, organizational methods, #SM, #SMM.
        # Following #business trends and developments.
        # Top 1% Kred."""
        #
        #text = """["San Franciscan, yogi, rubyist, entrepreneur, @RubyRogues panelist, organizer of Golden Gate RubyConf", "Rubyist, motorcycle racer, cheapskate.\r\nDeveloper of Sidekiq http://t.co/ngmJl4Giae\r\nTech guy at @TheClymb", "GitHub Cofounder"]"""
        #
        #text = """San Franciscan, yogi, rubyist, entrepreneur, @RubyRogues panelist, organizer of Golden Gate RubyConf"""
        #
        #text = """Rubyist, motorcycle racer, cheapskate.\r\nDeveloper of Sidekiq http://t.co/ngmJl4Giae\r\nTech guy at @TheClymb"""
        #
        #text = """GitHub Cofounder"""
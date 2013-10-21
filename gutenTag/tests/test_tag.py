import unittest
from nose.tools import *
from ..tagger import Tagger


class TestTagger(unittest.TestCase):
    @staticmethod
    def test_tag_buddha():
        text = """The Buddha, the Godhead, resides quite as comfortably in the circuits of a digital
        computer or the gears of a cycle transmission as he does at the top of a mountain
        or in the petals of a flower. To think otherwise is to demean the Buddha...which is
        to demean oneself."""
        expected = 'buddha, godhead, circuit, digital, computer, gear, cycle, transmission, mountain, petal, ' + \
                   'flower, buddha, demean, oneself'
        assert_equals(Tagger.tag(text), expected)

    @staticmethod
    def test_tag_tillirix():
        text = """Marketaire.com  Founder - Internet marketing strategies & tactics. SEO, SEM, SMM. Let's do this.
        Toronto, Ontario, Canada . marketaire.com"""
        expected = 'marketaire, com, founder, internet, marketing, strategy, tactic, seo, sem, smm, let, toronto, ' + \
                   'ontario, canada, marketaire, com'
        assert_equals(Tagger.tag(text), expected)

        text = """SEM SEO SMM PPC Performance Suchmaschinen Marketing sponsored listings affiliate adwords paid
        search social ROI tracking; twitterbot; follow @ressmann my human"""
        expected = 'seo, smm, ppc, performance, suchmaschinen, marketing, listing, adwords, search, social, roi, ' + \
                   'tracking, twitterbot, follow, ressmann, human'
        assert_equals(Tagger.tag(text), expected)

        text = """#Technology, science, self-development, organizational methods, #SM, #SMM.
        Following #business trends and developments.
        Top 1% Kred."""
        expected = 'technology, science, organizational, method, sm, smm, following, business, trend, ' + \
                   'development, top, kred'
        assert_equals(Tagger.tag(text), expected)

    @staticmethod
    def test_tag_joshowens():
        text = """San Franciscan, yogi, rubyist, entrepreneur, @RubyRogues panelist,
        organizer of Golden Gate RubyConf"""
        expected = 'san, franciscan, yogi, rubyist, entrepreneur, rubyrogues, organizer, golden, gate, rubyconf'
        assert_equals(Tagger.tag(text), expected)

        text = """Rubyist, motorcycle racer, cheapskate.
        Developer of Sidekiq http://t.co/ngmJl4Giae
        Tech guy at @TheClymb"""
        expected = 'rubyist, motorcycle, racer, developer, sidekiq, http, co, ngmjl4giae, tech, guy, theclymb'
        assert_equals(Tagger.tag(text), expected)

        text = """GitHub Cofounder"""
        expected = 'github, cofounder'
        assert_equals(Tagger.tag(text), expected)

    @staticmethod
    def test_tag_follow():
        text = """follow follows followed following follower followers"""
        expected = 'follow, follower'
        assert_equals(Tagger.tag(text), expected)

        text = """follow follows followed following followings follower followers"""
        expected = 'follow, following, follower'
        assert_equals(Tagger.tag(text), expected)

        text = """Follow me back!"""
        expected = 'follow'
        assert_equals(Tagger.tag(text), expected)

        text = """I have a large following in Hungary and a small following in the USA."""
        expected = 'hungary, usa'
        assert_equals(Tagger.tag(text), expected)
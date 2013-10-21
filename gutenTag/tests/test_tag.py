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
        expected = 'buddha, godhead, circuit, digit, comput, gear, cycl, transmiss, mountain, petal, flower, ' + \
                   'buddha, demean, oneself'
        assert_equals(Tagger.tag(text), expected)

    @staticmethod
    def test_tag_tillirix():
        text = """Marketaire.com  Founder - Internet marketing strategies & tactics. SEO, SEM, SMM. Let's do this.
        Toronto, Ontario, Canada . marketaire.com"""
        expected = 'marketair, com, founder, internet, market, strategi, tactic, seo, sem, smm, let, toronto, ' + \
                   'ontario, canada, marketair, com'
        assert_equals(Tagger.tag(text), expected)

        text = """SEM SEO SMM PPC Performance Suchmaschinen Marketing sponsored listings affiliate adwords paid
        search social ROI tracking; twitterbot; follow @ressmann my human"""
        expected = 'seo, smm, ppc, perform, suchmaschinen, market, list, adword, search, social, roi, track, ' + \
                   'twitterbot, follow, ressmann, human'
        assert_equals(Tagger.tag(text), expected)

        text = """#Technology, science, self-development, organizational methods, #SM, #SMM.
        Following #business trends and developments.
        Top 1% Kred."""
        expected = 'technolog, scienc, organiz, method, sm, smm, follow, busi, trend, develop, top, kred'
        assert_equals(Tagger.tag(text), expected)

    @staticmethod
    def test_tag_joshowens():
        text = """San Franciscan, yogi, rubyist, entrepreneur, @RubyRogues panelist,
        organizer of Golden Gate RubyConf"""
        expected = 'san, franciscan, yogi, rubyist, entrepreneur, rubyrogu, organ, golden, gate, rubyconf'
        assert_equals(Tagger.tag(text), expected)

        text = """Rubyist, motorcycle racer, cheapskate.
        Developer of Sidekiq http://t.co/ngmJl4Giae
        Tech guy at @TheClymb"""
        expected = 'rubyist, motorcycl, racer, develop, sidekiq, http, co, ngmjl4giae, tech, guy, theclymb'
        assert_equals(Tagger.tag(text), expected)

        text = """GitHub Cofounder"""
        expected = 'github, cofound'
        assert_equals(Tagger.tag(text), expected)
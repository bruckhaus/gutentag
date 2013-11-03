import unittest
from nose.tools import *
from ..tagger import Tagger
import subprocess


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

    @staticmethod
    def test_tag_file():
        p = subprocess.Popen(["python", "./gutenTag/tagger.py", "./doc/george_washingtons_journal.txt"],
                             stdout=subprocess.PIPE)
        out, err = p.communicate()
        expected = 'william, findley, david, redick, committee, safety, met, month, parkinson, ferry, camp, resolution, committee, information, state, thing, western, county, pennsylvania, washington, fayette, westd, alligany, order, march, army, oclock, meeting, person, presence, govr, howell, new, jersey, secretary, treasury, colo, hamilton, mr, dandridge, govr, mifflin, acct, business, deputy, resolution, information, disposition, state, matter, county, men, mr, findley, information, part, county, mr, reddick, knowledge, part, county, substance, mr, findleys, communication, viz, people, part, law, public, office, collection, tax, spirit, still, intimating, present, people, office, inspection, pitsburgh, protection, influence, garrison, distiller, enter, still, civil, authority, tone, instance, ignorance, general, want, information, people, thing, conception, excise, law, opposition, law, government, officer, government, situation, life, sometime, go, scene, mr, redicks, information, last, recital, wch, sentiment, situation, opposition, government, whilst, frenzy, height, arm, side, night, morning, occasion, defence, person, property, long, time, riot, distrust, friend, sentiment, whisper, bolder, strength, general, disposition, law, instance, magistrate, people, county, opposition, excise, law, dereliction, part, state, troop, march, purpose, coercion, acct, troop, tale, governmental, men, property, rate, order, country, go, detroit, person, consequence, amnesty, opposition, law, men, property, intention, army, round, ammunition, western, country, mr, findley, resentment, army, treatment, people, disagreeable, consequence, account, march, wish, people, proof, unequivocal, submission, object, hearing, wish, governmt, people, county, sense, duty, mild, lenient, purpose, sober, reflection, fatal, consequence, conduct, commissioner, amongst, time, opposition, law, coercion, wou, dernier, resort, season, year, preparation, pace, proposition, transaction, people, proceeding, government, measure, adoption, expensive, inconvenient, point, view, support, law, object, first, magnitude, part, expense, nothing, unequivocal, proof, absolute, submission, march, army, western, order, government, obedience, law, impunity, proof, justice, example, meaning, interview, oclock, noon, second, meeting, repeti, ti, forenoon, principal, character, western, opposition, proposition, street, next, day, mr, redick, time, disclosure, time, meeting, oclock, afternoon, place, david, bradford, person, former, conversation, meeting, people, deputy, army, point, march, country, fresh, evidence, sincerity, disposition, whatever, objection, gun, consequence, case, possible, care, troop, offering, insult, damage, law, amnesty, person, property, treatment, rest, conduct, army, executioner, offender, military, tribunal, civil, offence, thus, matter\n'
        assert_equals(out, expected)
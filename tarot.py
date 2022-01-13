import random
deck = {
	0: {"name": "The Fool", "meaning": {"Upright": "Beginnings, Innocence, Spontaneity, A Free Spirit", "Reversed": "Holding Back, Recklessness, Risk Taking"}}
	1: {"name": "The Magician", "meaning": {"Upright": "Manifestation, Resourcefulness, Power, Inspired Action", "Reversed": "Manipulation, Poor Planning, Untapped Talents"}}
	2: {"name": "The High Priestess", "meaning": {"Upright": "Intuition, Sacred Knowledge, Divine Feminine, The Subconscious Mind", "Reversed": "Secrets, Disconnected from Intuition, Withdrawl and Silence"}}
	3: {"name": "The Empress", "meaning": {"Upright": "Femininity, Beauty, Nature, Nurturing, Abundance", "Reversed": "Creative Block, Dependence on Others"}}
	4: {"name": "The Emperor", "meaning": {"Upright": "Authority, Establishment, Structure, A Father Figure", "Reversed": "Domination, Excessive Control, Lack of Discipline, Inflexibility"}}
	5: {"name": "The Heirophant", "meaning": {"Upright": "Spiritual Wisdom, Religious Beliefs, Conformity, Tradition, Institutions", "Reversed": "Personal Beliefs, Freedom, Challenging the Status Quo"}}
	6: {"name": "The Lovers", "meaning": {"Upright": "Love, Harmony, Relationships, Values Alignment, Choices", "Reversed": "Self Love, Disharmony, Imbalance, Misalignment of Values"}}
	7: {"name": "The Chariot", "meaning": {"Upright": "Control, Willpower, Success, Action, Determination", "Reversed": "Self Discipline, Opposition, Lack of Direction"}}
	8: {"name": "Strength", "meaning": {"Upright": "Strength, Courage, Persuasion, Influence, Compassion", "Reversed": "Inner Strength, Self Doubt, Low Energy, Raw Emotion"}}
	9: {"name": "The Hermit", "meaning": {"Upright": "Soul Searching, Introspection, Being Alone, Inner Guidance", "Reversed": "Isolation, Loneliness, Withdrawl"}}
	10: {"name": "Wheel of Fortune", "meaning": {"Upright": "Good Luck, Karma, Life Cycles, Destiny, A Turning Point", "Reversed": "Bad Luck, Resistance to Change, Breaking Cycles"}}
	11: {"name": "Justice", "meaning": {"Upright": "Justice, Fairness, Truth, Cause and Effect, Law", "Reversed": "Unfairness, Lack of Accountability, Dishonesty"}}
	12: {"name": "The Hanged Man", "meaning": {"Upright": "Pause, Surrender, Letting Go, New Perspectives", "Reversed": "Delays, Resistance, Stalling, Indecision"}}
	13: {"name": "Death", "meaning": {"Upright": "Endings, Change, Transformation, Transition", "Reversed": "Resistance to Change, Personal Transformation, Inner Purging"}}
	14: {"name": "Temperance", "meaning": {"Upright": "Balance, Moderation, Patience, Purpose", "Reversed": "Imbalance, Excess, Self Healing, Re-Alignment"}}
	15: {"name": "The Devil", "meaning": {"Upright": "Shadow Self, Attachment, Addiction, Restriction, Sexuality", "Reversed": "Releasing Limiting Beliefs, Exploring Dark Thoughts, Detachment"}}
	16: {"name": "The Tower", "meaning": {"Upright": "Sudden Change, Upheaval, Chaos, Revelation, Awakening", "Reversed": "Personal Transformation, Fear of Change, Averting Disaster"}}
	17: {"name": "The Star", "meaning": {"Upright": "Hope, Faith, Purpose, Renewal, Spirituality", "Reversed": "Lack of Faith, Despair, Self Trust, Disconnection"}}
	18: {"name": "The Moon", "meaning": {"Upright": "Illusion, Fear, Anxiety, Subconscious, Intuition", "Reversed": "Release of Fear, Repressed Emotion, Inner Confusion"}}
	19: {"name": "The Sun", "meaning": {"Upright": "Positivity, Fun, Warmth, Success, Vitality", "Reversed": "Inner Child, Feeling Down, Overly Optimistic"}}
	20: {"name": "Judgement", "meaning": {"Upright": "Judgement, Rebirth, Inner Calling, Absolution", "Reversed": "Self Doubt, Inner Critic, Ignoring the Call"}}
	21: {"name": "The World", "meaning": {"Upright": "Completion, Integration, Accomplishment, Travel", "Reversed": "Seeking Personal Closure, Short Cuts, Delays"}}
	22: {"name": "Ace of Cups", "meaning": {"Upright": "Love, New Relationships, Complassion, Creativity", "Reversed": "Self Love, Intuition, Repressed Emotions"}}
	23: {"name": "Two of Cups", "meaning": {"Upright": "Unified Love, Partnership, Mutual Attraction", "Reversed": "Self Love, Break-Ups, Disharmony, Distrust"}}
	24: {"name": "Three of Cups", "meaning": {"Upright": "Celebration, Friendship, Creativity, Collaborations", "Reversed": "Independence, Alone Time, Hardcore Partying"}}
	25: {"name": "Four of Cups", "meaning": {"Upright": "Meditation, Contemplation, Apathy, Reevaluation", "Reversed": "Retreat, Withdrawl, Checking in for Alignment"}}
	26: {"name": "Five of Cups", "meaning": {"Upright": "Regret, Failure, Disappointment, Pessimism", "Reversed": "Personal Setbacks, Self Forgiveness, Moving On"}}
	27: {"name": "Six of Cups", "meaning": {"Upright": "Revisiting the Past, Childhood Memories, Innocence, Joy", "Reversed": "Living in the Past, Forgiveness, Lacking Playfulness"}}
	28: {"name": "Seven of Cups", "meaning": {"Upright": "Opportunities, Choices, Wishful Thinking, Illusion", "Reversed": "Alignment, Personal Values, Overwhelmed by Choices"}}
	29: {"name": "Eight of Cups", "meaning": {"Upright": "Disappointment, Abandonment, Withdrawl, Escapism", "Reversed": "Trying One More Time, Indecision, Aimless Drifting, Walking Away"}}
	30: {"name": "Nine of Cups", "meaning": {"Upright": "Contentment, Satisfaction, Gratitude, Wish Come True", "Reversed": "Inner Happiness, Materialism, Dissatisfaction, Indulgence"}}
	31: {"name": "Ten of Cups", "meaning": {"Upright": "Divine Love, Blissful Relationships, Harmony, Alignment", "Reversed": "Disconnection, Misaligned Values, Struggling Relationships"}}
	32: {"name": "Page of Cups", "meaning": {"Upright": "Creative Opportunities, Intuitive Messages, Curiosity, Possibility", "Reversed": "New Ideas, Doubting Intuition, Creative Blocks, Emotional Immaturity"}}
	33: {"name": "Knight of Cups", "meaning": {"Upright": "Creativity, Romance, Charm, Imagination, Beauty", "Reversed": "Overactive Imagination, Unrealistic, Jealous, Moody"}}
	34: {"name": "Queen of Cups", "meaning": {"Upright": "Compassionate, Caring, Emotionally Stable, Intuitive, In Flow", "Reversed": "Inner Feelings, Self Care, Self Love, Co-Dependancy"}}
	35: {"name": "King of Cups", "meaning": {"Upright": "Emotionally Balanced, Compassionate, Diplomatic", "Reversed": "Self Compassion, Inner Feelings, Moodiness, Emotionally Manipulative"}}
	36: {"name": "Ace of Swords", "meaning": {"Upright": "Breakthroughs, New Ideas, Mental Clarity, Success", "Reversed": "Inner Clarity, Re-Thinking an Idea, Clouded Judgement"}}
	37: {"name": "Two of Swords", "meaning": {"Upright": "Difficult Decisions, Weighing up Options, An Impasse, Avoidance", "Reversed": "Indecision, Confusion, Information Overload, Stalemate"}}
	38: {"name": "Three of Swords", "meaning": {"Upright": "Heartbreak, Emotional Pain, Sorrow, Grief, Hurt", "Reversed": "Negative Self Talk, Releasing Pain, Optimism, Forgiveness"}}
	39: {"name": "Four of Swords", "meaning": {"Upright": "Rest, Relaxation, Meditation, Contemplation, Recuperation", "Reversed": "Exhaustion, Burnout, Deep Contemplation, Stagnation"}}
	40: {"name": "Five of Swords", "meaning": {"Upright": "Conflict, Disagreements, Competition, Defeat, Winning at All Costs", "Reversed": "Reconciliation, Making Amends, Past Resentment"}}
	41: {"name": "Six of Swords", "meaning": {"Upright": "Transition, Change, Rite of Passage, Releasing Baggage", "Reversed": "Personal Transition, Resistance to Change, Unfinished Business"}}
	42: {"name": "Seven of Swords", "meaning": {"Upright": "Betrayal, Deception, Getting Away with Something, Acting Strategically", "Reversed": "Imposter Syndrome, Self Deceit, Keeping Secrets"}}
	43: {"name": "Eight of Swords", "meaning": {"Upright": "Negative Thoughts, Self Imposed Restriction, Imprisonment, Victim Mentality", "Reversed": "Self Limiting Beliefs, Inner Critic, Releasing Negative Thoughts, Open to New Perspectives"}}
	44: {"name": "Nine of Swords", "meaning": {"Upright": "Anxiety, Worry, Fear, Depression, Nightmares", "Reversed": "Inner Turmoil, Deep Seated Fears, Secrets, Releasing Worry"}}
	45: {"name": "Ten of Swords", "meaning": {"Upright": "Painful Endings, Deep Wounds, Betrayal, Loss, Crisis", "Reversed": "Recovery, Regeneration, Resisting an Inevitable End"}}
	46: {"name": "Page of Swords", "meaning": {"Upright": "New Ideas, Curiosity, Thirst for Knowledge, New Ways of Communicating", "Reversed": "Self Expression, All Talk and No Action, Haphazard Action, Haste"}}
	47: {"name": "Knight of Swords", "meaning": {"Upright": "Ambitious, Action Oriented, Driven to Succeed, Fast Thinking", "Reversed": "Restless, Unfocused, Impulsive, Burnout"}}
	48: {"name": "Queen of Swords", "meaning": {"Upright": "Independent, Unbiased Judgement, Clear Boundaries, Direct Communication", "Reversed": "Overly Emotional, Easily Influenced, Bitchy, Cold Hearted"}}
	49: {"name": "King of Swords", "meaning": {"Upright": "Mental Clarity, Intellectual Power, Authority, Truth", "Reversed": "Quiet Power, Inner Truth, Misuse of Power, Manipulation"}}
	50:
}
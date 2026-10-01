# Maintenance

This repository is stable only if the skill rules and the production template stay aligned.

## Safe Update Areas

You can safely update these without changing the repo’s identity:

- README wording
- examples
- story samples
- explanatory docs
- example prompts

## High-Risk Update Areas

Change these carefully because they affect production consistency:

- `skills/titi-story/SKILL.md`
- the fixed section order
- the learning intro block
- shot count
- dialogue summary shape
- character lock rules
- `愿望灯` constraints

## Before Changing The Skill

Ask:

1. is this a real workflow change or just a one-off story preference?
2. does this belong in the permanent skill or only in one episode prompt?
3. will this break old examples or new episodes?

If the change is one-off, keep it out of the skill and place it in the user prompt instead.

## Regression Checklist

After any skill update, test a known example and a different core word. Read the generated output, not just the rule text. Also check local links, HTML desktop/mobile display, navigation and checklist interaction. Verify:

- `学习单词提示镜头分解` still appears
- `文字表现建议` still appears
- `正片镜头分解` still appears
- there are exactly `12` main shots
- the story uses only `1` core word
- main story is four 15-second blocks, three frames each; learning intro is 8 seconds and repeat-along is up to 8 seconds; greeting and farewell are additional
- board layout is two rows by six columns, overall16:9, each frame9:16, outer padding only
- each block has a complete video prompt and transition states
- every frame has English dialogue; exactly three standalone core-word utterances with response pauses occur in the main story
- the sole front-left waist lantern remains visible while off and on; incantation precedes activation
- full bilingual record covers five segments; matching text selects greeting, one actual English intro word, all main dialogue, two actual English repeat-along words, and farewell
- do not globally remove phrases such as Let’s go! that also occur in the main story
- repeat-along has one Chinese word, two English words, response gaps and a warm question within 8 seconds
- each main block has motivated camera movement; full story uses at least three movement types without physical scale drift or hiding the lantern
- a second core word does not inherit HEAD-specific rabbit/rain/ear rules
- there is still no background music
- the ending is still a child-friendly funny twist

## Recommended Test Prompt

```text
Use $titi-story to write a complete TiTi story for BAG. A friend uses a bag to carry pinecones home.
```

## Single Source of Rules

The installable skill and references under skills/titi-story are the normative source. Keep HTML, README, templates, SOP and examples aligned. Historical episode-one scripts are retained as historical creative material, not current output templates. Do not overwrite an installed skill or publish a candidate until the user confirms that step.

## Versioning Guidance

Use simple semantic intent for repo versions:

- patch: doc clarifications, examples, wording improvements
- minor: new supporting docs, templates, examples, non-breaking rule clarifications
- major: output format changes, structure changes, command changes, or story-rule changes that alter expected downstream production

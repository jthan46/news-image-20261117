# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/jthan46/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/jthan46/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image sums up Tuesday 17 November 2026: Ukraine's strike partly collapses the Kerch Bridge, Iran hits a US base in Bahrain, Trump in Asia for Xi–Putin talks, the US loses measles-free status, France strikes, and a Gaza aid call.

The entry is a single front-page-style image, "THE WORLD IN ONE IMAGE", with a large banner naming the day — TUESDAY · 17 NOVEMBER 2026 — over six illustrated story panels, each with a short factual headline as reported that day. The panel illustrations are original AI-generated editorial artwork (in `assets/`), and the page is composed programmatically with real fonts by `tools/compose.py` (Python PIL), so every word is crisp. `main.ts` copies the finished `entry.png` to the output directory.

## The stories

- **Kerch Bridge partly collapses in Ukraine strike** — Ukraine said a section of the Kerch Bridge to Crimea collapsed after a weeks-long strike operation; President Zelenskyy hailed the "unprecedented" attack. Source: BBC, "Putin's Crimean Bridge partly collapses as Zelensky hails 'unprecedented' attack by Ukraine" (17 Nov 2026).
- **Iran strikes US base in Bahrain for a third time in days** — Iran fired at a US facility in Bahrain, its third such attack in days, and the US confirmed a retaliatory strike on Qeshm Island. Sources: PBS NewsHour (17 Nov 2026); Daily Baku, "US confirms strike on Qeshm Island" (17 Nov 2026).
- **Trump in Asia ahead of talks with Xi and Putin** — the US president travelled in Asia ahead of talks with China's and Russia's presidents, the three leaders set to meet at the APEC summit in Shenzhen. Source: BBC, "Trump in Asia ahead of talks with Russian and Chinese presidents" (17 Nov 2026).
- **US loses measles-free status after 26 years** — the United States lost its measles elimination status amid record case numbers, with over 5,400 cases and 10 deaths reported this year, a 40-year high. Source: BBC, "US loses measles elimination status after 26 years amid record case numbers" (17 Nov 2026).
- **146,000 march as France strikes over cost of living** — unions held a second nationwide strike, with 146,000 people protesting across France over living costs. Source: Daily Baku, "146,000 protest across France as unions strike over living costs" (17 Nov 2026).
- **Four nations urge Israel to open Gaza aid crossings** — the United Kingdom, Australia, Canada and Italy issued a joint statement calling on Israel to allow rapid humanitarian access into Gaza, as UN agencies warned of a worsening winter emergency. Source: Asas Press, "World News Digest: Top Stories of November 17, 2026" (17 Nov 2026).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=bjydwhj1&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>

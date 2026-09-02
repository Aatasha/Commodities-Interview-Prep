# Market-View Question Bank

How to use: these questions train you to defend a view under pressure, which is the part of a Glencore, Trafigura or Vitol interview that most candidates fail. The interviewer does not care whether you are right; they care whether you have a view, can name the two or three things driving it, know what would make you change it, and can turn it into a trade with a defined risk. Every model answer below therefore describes the STRUCTURE of a strong answer (view → drivers → what changes my mind → expression as outright, spread or option) rather than asserting a direction, because the right direction depends on the day. Eight questions (marked TEMPLATED) contain placeholders in double braces such as `{{brent_m1_m2}}`; the mock-interview skill substitutes these from the latest file in `briefs/`. If you are practising by hand, open the latest brief and fill them in yourself. Never quote a number from memory as "today's" in an interview — say "as of this morning's brief" and give the number.

Placeholders used: `{{brent_flat}}`, `{{brent_m1_m2}}`, `{{brent_wti}}`, `{{crack_321}}`, `{{ttf_minus_hh}}`, `{{copper_flat}}`, `{{top_oil_story}}`, `{{top_metals_story}}`, `{{glencore_news}}`.

Coverage:
- Evergreen flat-price views: Brent, copper, coal, LNG, freight
- Base/bull/bear construction with probabilities and drivers
- Reactive scenarios: OPEC+ decisions, hurricanes, Hormuz, China stimulus, EV demand shifts
- Templated questions keyed to the latest brief: spreads, cracks, gas arbs, top stories, Glencore news
- Expressing a view in a trade: outright vs spread vs option, sizing to risk
- Positioning, "what is the market wrong about", and defending under attack

---

### Q1. Where is Brent in six months and why? Give me a base, bull and bear case with drivers.
**Difficulty:** 1
**Model answer:**
- Open with a number and a probability: "Base case $X, roughly 55% weight; bull $X+15, 25%; bear $X−15, 20%." Anchor to the current price and curve from the brief, not a memorised figure.
- Base case drivers (pick three): OPEC+ policy path and spare capacity; non-OPEC supply growth (US shale, Brazil, Guyana, Canada); demand growth (China, India, aviation, petrochemicals) against the macro backdrop; and inventories relative to the five-year range.
- Bull case: a supply disruption (sanctions enforcement, Middle East escalation, hurricane season), OPEC+ discipline plus faster demand, or draws that push the curve into steep backwardation.
- Bear case: OPEC+ unwinding cuts into weak demand, a recession or Chinese slowdown, US production surprising to the upside, or a sanctions relaxation returning barrels.
- What changes my mind: name two observable indicators with thresholds — e.g. OECD stocks vs the five-year average, the M1-M2 spread flipping sign, refinery margin collapse, a change in OPEC+ communication.
- Expression: if you believe the base case is tightness, a time-spread (long M1-M3) has better risk-reward than an outright; if you believe in the tails, a call spread or put spread limits premium; only go outright if you accept 2-3% daily vol on your capital.
- Close by acknowledging the forward curve already embeds a view; you are arguing the curve is wrong, not predicting from zero.
**Pushback:**
- "The curve is already backwardated $X. Isn't your bull case priced in?" (Distinguish the spot-level view from the roll: in backwardation a long outright loses the roll; a long spread only wins if backwardation steepens further.)
- "Give me the single number you'd bet your bonus on and what stops you out." (Be specific: level, stop, time horizon.)
**Red flags:** A single number with "because of geopolitics", no probabilities, no conditions for being wrong.

### Q2. Give me a bull and bear case for copper over twelve months.
**Difficulty:** 2
**Model answer:**
- Frame it as a balance: mine supply growth (a few large projects, grade decline, disruptions in Chile/Peru/DRC/Panama-type events) versus demand (Chinese property and grid, global electrification, data-centre power build, EVs) with exchange stocks as the tell.
- Bull: supply disruptions running above the historical ~5% allowance, low visible inventories across LME/SHFE/COMEX, Chinese grid capex, tariff-driven stockpiling in the US pulling metal out of the global pool, TC/RCs at lows confirming concentrate scarcity.
- Bear: Chinese property drag and weak fabricator orders, scrap substitution at high prices, demand destruction, dollar strength, a macro shock, or the arrival of new mine supply and a rebuild in exchange stocks; a contango returning to full carry.
- What changes my mind: Yangshan/CIF China premium direction, SHFE vs LME arb, cancelled warrants, Chinese refined imports, and the cash-3M spread.
- Expression: a bull who worries about macro buys a call spread or a cash-3M spread rather than outright; a bear who fears squeezes sells rallies via put spreads not naked shorts near prompts. Note the regional arb (COMEX-LME) as a separate trade from the flat price.
- Time horizon matters: twelve months is long enough for supply to respond; state where in the year you expect the pinch.
**Pushback:**
- "Why is copper different from other base metals right now?" (Concentrate constraint and electrification demand vs aluminium's energy-driven cost curve and nickel's Indonesian supply glut.)
- "What's your view on the COMEX-LME spread and how would you trade it?" (Depends on tariff policy — check the brief; a wide premium pulls metal into the US and hollows out LME stocks, which is bullish LME spreads.)
**Red flags:** "Copper is bullish because of the energy transition" with nothing about supply, stocks or timing.

### Q3. OPEC+ has just announced a surprise 1 million b/d production cut. How does the Brent curve move, and what else moves?
**Difficulty:** 2
**Model answer:**
- First-order: flat price gaps up (a 1 mb/d cut on a ~100 mb/d market is ~1% of supply, typically a $3-6 initial move depending on positioning and whether the market believes compliance). The front of the curve rises more than the back: backwardation steepens because the cut hits prompt barrels while deferred prices are anchored by shale response and demand elasticity.
- Second-order: the barrels cut are medium sour, so Dubai strengthens vs Brent — Brent-Dubai EFS narrows; sour differentials (Urals, Basrah, Arab Medium OSPs) firm; heavy-light narrows, hurting coker economics.
- Products: crude up faster than products initially, so cracks compress; then refiners cut runs if margins go negative, which re-widens cracks.
- Freight: fewer Middle East VLCC liftings → MEG-Asia VLCC rates fall.
- Positioning check: if speculators were short, the move overshoots; watch the CFTC/ICE COT in the brief.
- What changes the view: compliance data (tanker tracking, secondary sources), whether the cut is a response to demand weakness (bearish signal beneath the headline), and Saudi OSP changes.
- Trade expression: long M1-M3 spread or long EFS-narrowing (sell Brent, buy Dubai) rather than outright long into a gap; or sell put spreads to monetise the vol spike.
**Pushback:**
- "Why did the market sell off two days after the last surprise cut?" (Cuts that respond to demand weakness confirm the weakness; and unwinding of short covering. Distinguish headline from balance.)
- "What does this do to Glencore's business?" (Sour crude flows to Asia, freight rates, differentials — Marketing volatility is generally good; Industrial coal and copper are unaffected directly.)
**Red flags:** Only says "price goes up" with no curve, differential or product effect.

### Q4. OPEC+ unwinds its voluntary cuts faster than the market expected. Talk me through the next three months.
**Difficulty:** 2
**Model answer:**
- Structure: quantify the barrels (voluntary cuts have historically been a few mb/d across a handful of members; the brief will say what remains), the timing of the monthly increments, and the realistic volume (some members were already overproducing, so the real increase is smaller than the headline).
- Curve: front spreads flatten or flip to contango first because the incremental barrels are prompt; deferred prices react less. Flat price falls on the announcement and then the market tests where shale's break-even provides a floor.
- Differentials: sour barrels cheapen — EFS widens, Urals/Basrah discounts widen, OSPs cut. Coker margins improve. Asian refiners switch back to term Middle East crude, reducing demand for Atlantic-basin barrels and closing the West-East arb.
- Freight: MEG-Asia VLCC rates rise on more liftings.
- What changes my mind: whether the unwind is paired with a demand narrative (seasonal), whether OPEC+ compensation cuts offset it, and how quickly inventories build (watch OECD and floating storage).
- Expression: short M1-M2 (bet on contango), long EFS, or buy puts if you fear a disorderly market-share war; a spread expresses the barrel timing, an option expresses the tail.
**Pushback:**
- "What price level makes OPEC+ reverse course?" (Talk about fiscal break-evens and market-share strategy — the answer depends on their objective, which you should infer from their communication in the brief.)
- "Who suffers more, a US shale producer or a West African producer?" (West African: they sell light sweet into Asia against cheaper sour, and their differentials to Dated widen; shale hedges and has lower delivered cost to the USGC.)
**Red flags:** Cannot distinguish headline volume from effective volume.

### Q5. A Category 4 hurricane shuts 1.5 million b/d of Gulf Coast refining and the Houston Ship Channel for two weeks. What moves and how?
**Difficulty:** 2
**Model answer:**
- Split the shock into crude and products. Refinery outage removes crude demand (bearish WTI, Brent-WTI widens as US crude backs up) and product supply (bullish gasoline and diesel cracks, especially RBOB into the US East Coast and Latin America).
- Export disruption: USGC crude exports (several mb/d) and product exports stop, so Atlantic-basin crude tightens (supportive of Dated Brent and the DFL) while Cushing and Gulf Coast crude weaken; the same for products in reverse — Europe and Asia are called on to supply diesel and gasoline to the Americas.
- Freight: Aframax and MR rates spike for vessels positioned to serve the Americas; demurrage rises.
- Curve: WTI M1-M2 weakens; RBOB and ULSD prompt spreads spike; the 3-2-1 crack jumps then normalises as refineries restart.
- What changes my mind: restart pace (days vs weeks), damage to pipelines and power, whether production in the Gulf of Mexico is also shut (which offsets the crude bearishness).
- Expression: long cracks vs short WTI spread; long RBOB-Brent or long ULSD transatlantic arb; or sell WTI-Brent spread; avoid outright flat price because the two effects cancel.
**Pushback:**
- "Offshore production of 1.5 mb/d is also shut. Now what's your net crude view?" (Roughly balanced: lost refinery demand ≈ lost production; the trade stays in cracks and spreads, not flat price.)
- "How would you make money physically rather than on paper?" (Reposition product cargoes from Europe to the US East Coast and Latin America, fix MR freight early, and buy distressed crude at the Gulf Coast to store or export once the channel reopens.)
**Red flags:** Says "oil goes up" without distinguishing crude from products.

### Q6. A serious Middle East escalation disrupts shipping through the Strait of Hormuz for a week. Walk me through the market reaction.
**Difficulty:** 3
**Model answer:**
- Quantify: roughly a fifth of global oil supply and a similar share of LNG (Qatar) transits Hormuz; a full week's disruption is tens of millions of barrels delayed, not lost, unless production is shut in.
- Price path: violent spike in flat price and in the front spread (M1-M2 and Dubai spreads blow out), then a decay as tankers move and the market judges whether flows resume. Dubai strengthens vs Brent (EFS narrows or goes negative). JKM spikes on Qatari LNG risk.
- Freight: VLCC rates and war-risk insurance premiums jump; ships refuse to fix; owners reroute via the Saudi East-West pipeline to Yanbu and the UAE's Fujairah pipeline — those are the mitigants and their capacity (a few mb/d) is the limit.
- Products: Asian and European diesel cracks spike (Middle East is a large diesel exporter); jet follows.
- Positioning and volatility: implied vol doubles; options become expensive; the market then punishes anyone who bought protection late.
- What changes my mind: evidence of actual production shut-ins vs delays; whether the disruption escalates to infrastructure damage; naval escort signals; and how quickly insurers re-price.
- Expression: given the tail, a call spread or a long M1-M3 spread, funded partly by selling deferred vol; physically, cargoes already outside the Gulf become very valuable — the desk's job is optionality on timing and destination.
**Pushback:**
- "Why would you sell deferred vol in that situation?" (The back of the curve is anchored by spare capacity and demand destruction; the tail risk is concentrated in the front. Be ready to say when that is wrong: sustained infrastructure damage.)
- "After the spike, what's the trade?" (Fade the front spread once flows resume, keep an eye on the war-risk premium and stranded cargoes; the reversal is often as violent as the spike.)
**Red flags:** Treats delayed barrels as lost, or cannot name the pipeline bypasses.

### Q7. China announces a large stimulus for property and infrastructure. What does it mean for iron ore, copper and coal — and what do you actually believe?
**Difficulty:** 2
**Model answer:**
- Separate the headline from the transmission. Property stimulus historically lifts steel demand first (iron ore, met coal), then copper (wiring is late-cycle in construction) and thermal coal via power demand and cement.
- Immediate: iron ore and copper rally on the announcement; SHFE outperforms LME; the Yangshan premium and cancelled warrants tell you whether physical buying follows.
- Belief test: has Chinese property demand structurally rolled over (completions vs starts), so stimulus supports completions but not new starts? Then the copper effect is bigger than the steel effect. Is the money real (fiscal) or just credit encouragement (less effective)?
- Coal: infrastructure and industrial output lift power burn; the seaborne effect depends on domestic production and import policy, so 5,500 NAR into China moves more than NEWC 6,000.
- What changes my mind: credit data (TSF), steel mill margins (if negative, mills won't raise output), copper fabricator operating rates, and the SHFE-LME arb.
- Expression: if I believe the copper effect, long copper vs short iron ore; a cross-market spread that isolates the view. If I doubt the stimulus, sell the rally in iron ore via a put spread.
**Pushback:**
- "Why has the market stopped rallying on Chinese stimulus announcements?" (Repeated under-delivery; the market wants physical evidence — import volumes, premiums — not policy statements.)
- "What does this do for Glencore?" (Copper and coal are the two biggest Industrial earnings drivers; but ask about timing — a demand signal takes quarters to reach earnings.)
**Red flags:** "China stimulus is bullish everything."

### Q8. Several new US LNG export trains start up in the same year. Where do TTF and JKM go, and how does the US-Europe arb behave?
**Difficulty:** 2
**Model answer:**
- Quantify the supply wave from the brief (new US and Qatari capacity in a given period), and compare with demand growth (Asian coal-to-gas switching, European storage refill needs, industrial recovery). A supply wave usually pushes TTF and JKM down toward the marginal cost of the flexible supplier — US LNG at 1.15 × HH + shipping.
- Floor logic: if TTF falls below 1.15 × HH + variable shipping, US cargoes are cancelled and the floor holds; the liquefaction fee is sunk so it does not enter the floor.
- JKM-TTF: the spread must pay for the extra shipping to Asia; in oversupply it compresses, and Europe becomes the sink; in Asian demand surges it widens.
- Europe-specific: storage levels vs the injection schedule, Norwegian maintenance, remaining Russian pipeline volumes, and coal switching (compare TTF in $/MWh with API2 plus carbon) set the price band.
- What changes my mind: a Northern Hemisphere cold winter, a Qatari or Australian outage, or delays in trains reaching nameplate (they routinely slip).
- Expression: short TTF summer vs long winter (seasonal spread), long JKM-TTF if you think Asia absorbs the wave, or long HH-TTF spread as the arb margin compresses; a physical trader wants destination-flexible cargoes and shipping optionality.
**Pushback:**
- "TTF is trading close to HH-linked cost. Are you saying it can't go lower?" (It can — the floor is a variable-cost floor and can be breached short-term when storage is full; also HH itself can fall.)
- "How does this affect European coal?" (Gas-to-coal switching disappears; API2 loses a support and European coal demand falls, weighing on the API2-API4 spread.)
**Red flags:** Cannot convert between EUR/MWh and $/MMBtu or does not know the cancellation mechanics.

### Q9. Give me a twelve-month view on Newcastle thermal coal.
**Difficulty:** 2
**Model answer:**
- View with a range, e.g. "I expect 6,000 NAR to trade in a band around $X with a downward skew" — and a reason for the skew.
- Drivers: Chinese domestic production and import policy (China imports a few hundred million tonnes; small changes swing the seaborne balance); Indian power demand and stock levels; Japanese/Korean nuclear restarts; LNG price relative to coal in Asia; Australian weather (La Niña floods, rail outages) and Indonesian export controls; the tail of European demand.
- Supply discipline: new export mine investment is limited by ESG and financing constraints, so supply is inelastic upward — which supports prices in demand spikes.
- Quality spreads: watch the 6,000 vs 5,500 NAR spread; a widening spread means high-CV demand from Japan/Korea is outrunning Chinese/Indian low-CV demand.
- What changes my mind: a hot Asian summer, hydro shortfalls, a gas price spike (bullish); a Chinese production surge or Indian stock build (bearish).
- Expression: an ICE Newcastle calendar spread rather than outright; or long NEWC vs short API2 if you think Asia outperforms Europe; physically, position blending capacity to sell 5,500 NAR into India when the quality spread is narrow.
- Note Glencore's exposure: as a top seaborne exporter, coal has been one of its largest profit swings; be ready to discuss the strategic debate about keeping vs spinning out coal (check the latest news).
**Pushback:**
- "Why hasn't ESG-driven under-investment sent prices to the moon?" (Demand is also declining in the OECD; the balance is a race between supply and demand attrition.)
- "What's the coal-gas switching level in Asia?" (Convert JKM to $/MWh of power and compare with coal at plant efficiency; be able to do the arithmetic.)
**Red flags:** "Coal is dying" with no view on the next twelve months.

### Q10. EV adoption slows sharply. What does that do to cobalt, nickel and lithium, and who is hurt?
**Difficulty:** 2
**Model answer:**
- Distinguish the three: lithium is almost pure battery demand, so it is hit hardest; nickel's battery share is small relative to stainless and its price is driven by Indonesian supply; cobalt is a by-product (of copper in the DRC, of nickel in Indonesia) so its supply does not respond to its own price.
- Cobalt: demand slowdown plus by-product supply = persistent surplus unless the DRC restricts exports (it has used bans and quotas; check the latest). Prices then depend on policy and on payables for hydroxide. Chemistry shift to LFP (no cobalt, no nickel) compounds the demand story.
- Nickel: the Indonesian supply wave dominates; an EV slowdown matters at the margin for class-1 nickel and sulphate premiums.
- Who is hurt: high-cost lithium producers, integrated Chinese cathode makers, and any trader long unhedged inventory of intermediates (there is no liquid hedge for hydroxide).
- What changes my mind: policy (subsidies, tariffs, emissions rules), battery chemistry mix data, and Chinese EV sales rather than Western ones (China is most of the volume).
- Expression: few liquid instruments — LME nickel, CME lithium hydroxide and cobalt contracts with thin liquidity; a physical trader positions via offtake terms (payable percentages, quotational periods) rather than paper.
**Pushback:**
- "If cobalt supply is by-product, how does the price ever recover?" (Demand catch-up, policy restriction, stockpiling — e.g. strategic reserves — or a copper price collapse that closes DRC mines.)
- "Why does Glencore care about cobalt if it's a by-product?" (It is a large share of the value of DRC copper ore and Glencore is one of the biggest producers; also the reputational and compliance lens on DRC provenance.)
**Red flags:** Treating the three metals as one "battery metals" trade.

### Q11. Tighter sanctions enforcement on shadow-fleet tankers: what happens to VLCC rates and to crude differentials?
**Difficulty:** 2
**Model answer:**
- Mechanism: sanctioned tonnage cannot be used by mainstream charterers, so the compliant fleet gets tighter; sanctioned barrels need longer, more convoluted voyages (STS transfers, slow steaming), raising tonne-miles. Both push compliant VLCC/Aframax rates up.
- Crude: sanctioned grades (Urals, Iranian, Venezuelan) discount widens to attract buyers and cover the risk; non-sanctioned substitutes (Middle East sour, West African, US) firm — bullish EFS-narrowing if the substitutes are sour, bullish Atlantic sweet differentials if they are sweet.
- Refiners in India and China that ran discounted barrels lose margin; their bids shift to term Middle East crude.
- Products: if refined-product sanctions tighten too, distillate cracks in Europe firm.
- What changes my mind: evidence of enforcement (designations, insurance denials, port refusals) vs announcement; and whether alternative shipping (new shadow buyers, flag states) fills the gap within weeks.
- Expression: long freight (FFAs on TD3C), long Dubai vs Brent or long Urals-Brent spread if you think the discount overshoots and will narrow, or long diesel cracks. Physically: control compliant tonnage early.
**Pushback:**
- "Isn't tighter enforcement bearish flat price because demand for the affected crude falls?" (No — displaced barrels usually find a home at a discount; the flat-price effect depends on whether production is shut in, which it rarely is.)
- "How does Glencore's compliance function shape what you can trade here?" (Sanctions screening, KYC on counterparties and vessels, no dealing in designated cargoes; the trade is on the compliant side of the market.)
**Red flags:** Cannot link tonne-miles to freight rates.

### Q12. TEMPLATED — Brent M1-M2 is at {{brent_m1_m2}} in this morning's brief. Is that spread too wide, too narrow, or fair? Defend it.
**Difficulty:** 2
**Model answer:**
- State the number and its sign: contango or backwardation, and where it sits versus full carry (~$0.85-0.95/bbl/month at typical storage and rates) and versus the recent range.
- Fair-value logic: in backwardation, the spread reflects prompt scarcity — compare with visible inventory trends (OECD stocks, Cushing, floating storage) and the DFL. If stocks are drawing and the DFL is positive, a steep spread is justified; if stocks are flat and the spread is steep, it is positioning or a technical squeeze.
- In contango: compare against full carry; wider than carry means storage is filling and the spread should compress as tanks absorb barrels; narrower means the market is not paying to store yet.
- View: "I think it is [too wide/narrow/fair] because [two drivers]" with a target level and horizon.
- What changes my mind: the next inventory prints, refinery run changes, OPEC+ or sanctions news, and expiry-related flows.
- Expression: long or short the M1-M2 or M1-M3 spread with a size defined by $/bbl risk (each $0.10 on 500 lots is $50k), or a spread option if you expect a regime flip. Never express a spread view with an outright.
**Pushback:**
- "What has the spread averaged over the last year and why is now different?" (Use the brief; if you don't know the history, say how you'd find it and what you'd compare.)
- "The spread is steeply backwardated but the DFL is negative. Which do you trust?" (The DFL — physical prompt cargoes struggling to clear says the futures spread is paper-driven and vulnerable.)
**Red flags:** Reads the number back without a view or a comparison point.

### Q13. TEMPLATED — Brent-WTI is {{brent_wti}} today. Is the transatlantic arb open? What would you do?
**Difficulty:** 2
**Model answer:**
- Correct the benchmark: the arb is not Brent minus WTI Cushing, it is Brent (or the Dated grade a European refiner would buy) minus WTI at the Gulf Coast (Houston/MEH or Corpus) plus freight, port costs, financing and losses.
- Build the landed cost: WTI Houston (Cushing plus pipeline tariff and terminal fees, ~$1-2/bbl) + Aframax/Suezmax freight USGC-Europe (from the brief or recent fixtures, typically $2-4/bbl) + insurance/financing/losses (~$0.30-0.50) = landed Rotterdam. Compare with the price of a comparable European light sweet barrel (e.g. Forties or Dated plus differential).
- Adjust for quality (WTI Midland is lighter — a small premium or discount depending on refinery yield preferences and the sulphur spec).
- View: open, closed, or marginal, and what the marginal item is (usually freight).
- What changes my mind: a freight move (hurricane, Red Sea diversions), a Cushing stock change, a change in US export flows, or a shift in the Dated-futures relationship.
- Expression: if open, buy WTI Houston, sell Dated-linked CIF Rotterdam, fix a vessel, and hedge the Brent-WTI spread as futures; if closed, watch for widening — a long Brent-WTI spread position at the paper level is a way to own the arb before it opens.
**Pushback:**
- "Freight rises $1.50 tomorrow. Is your cargo still profitable?" (Show the sensitivity: on a 700,000 bbl Aframax, $1.50 is ~$1m; state whether that eats your margin.)
- "Why would a European refiner take WTI Midland over Forties?" (Yield, sulphur, price; know that Midland is now in the Dated basket so the relative pricing is transparent.)
**Red flags:** Treats a Cushing-based spread as the arb.

### Q14. TEMPLATED — The 3-2-1 crack is {{crack_321}}. Are refiners going to run harder, and what does that mean for crude and products over the next quarter?
**Difficulty:** 2
**Model answer:**
- Interpret the number: compare with the seasonal norm and the recent range (a "healthy" crack is a different number in summer driving season versus autumn maintenance). Split it into gasoline and distillate legs if the brief gives them — the composition tells you which product is tight.
- Refiner response: high cracks pull runs up (delayed maintenance, max throughput), which increases crude demand (supportive of WTI and Dated, of the front spread) and, with a lag of weeks, increases product supply that compresses the crack. Low cracks do the reverse.
- Constraints: US refining capacity has shrunk; run rates near 95% cannot rise much, so a high crack can persist. Outside the US, new Middle East and Chinese capacity adds product supply and pushes cracks down globally.
- View: "cracks [compress/hold] over the quarter because [runs rising / capacity constrained / demand seasonal]", with the crude implication separately.
- What changes my mind: EIA refinery utilisation prints, product stock levels, unplanned outages, and export demand (Latin America, West Africa).
- Expression: short crack via short products/long crude futures ratio (2 RBOB + 1 ULSD vs 3 WTI); or trade one leg (short gasoline crack into autumn); physically, a high crack says sell products and buy crude — the opposite when cracks are low.
**Pushback:**
- "Distillate is at a premium to gasoline. What's the fastest way for a refiner to swing yield?" (Cut FCC severity, adjust cut points, choose distillate-rich crudes; the swing is a few percentage points of yield, not a transformation.)
- "How does a trading house profit from a crack move without owning a refinery?" (Product storage and timing, blending components, arbs between regions where cracks differ, and paper crack spreads.)
**Red flags:** Cannot say what a 3-2-1 crack is composed of.

### Q15. TEMPLATED — TTF minus Henry Hub is {{ttf_minus_hh}} in $/MMBtu. What does that tell you about the US LNG arb, and where does it go?
**Difficulty:** 2
**Model answer:**
- Compute the arb: variable cost of a US cargo delivered to Europe is 1.15 × HH + shipping (~$1-2) + regas (~$0.30); the full cost adds the liquefaction fee ($2.25-3.50). If TTF minus HH exceeds the full cost, every contracted cargo lifts and the merchant margin is fat; if it only exceeds the variable cost, cargoes still lift but offtakers lose money on the fee; below variable cost, cargoes cancel.
- State where the number sits and what it implies for the next months: European storage trajectory, Asian competition (JKM-TTF), and the wave of new supply.
- Drivers: European storage vs targets, weather, Norwegian/Qatari outages, Asian demand pulling cargoes east, US production and Henry Hub itself (which can move independently on US weather and feedgas).
- View: "The spread [compresses/widens] toward $X because [drivers]".
- What changes my mind: storage fill pace, a cold-winter signal, JKM moving relative to TTF, feedgas data, and shipping rates.
- Expression: long or short the TTF-HH spread (both liquid; watch the currency and units), a JKM-TTF spread if the view is about destination, or a seasonal TTF spread; physically, sell destination flexibility to whoever values it most.
**Pushback:**
- "HH spikes on a US cold snap while TTF is flat. What happens to cargo flows?" (Nothing immediately — contracts still lift because the fee is sunk, but the merchant margin shrinks; only sustained HH strength above TTF minus variable shipping causes cancellations.)
- "What's your EUR/USD assumption and does it matter?" (Yes — TTF in EUR/MWh; a 5% currency move is roughly a 5% move in the $/MMBtu figure.)
**Red flags:** Doesn't convert units, or ignores the sunk-fee logic.

### Q16. TEMPLATED — The top oil story in this morning's brief is "{{top_oil_story}}". Give me the first-order and second-order effects, and a trade.
**Difficulty:** 3
**Model answer:**
- Summarise the story in one sentence and classify it: supply, demand, logistics, policy or positioning. That classification drives the rest.
- First-order: which price moves first and in which direction (flat price, front spread, a differential, a crack, freight)? Quantify it in barrels per day and put that in context of the ~100 mb/d market and current inventories.
- Second-order: who responds and how fast — OPEC+, shale, refiners, freight owners, governments (SPR releases, export bans), and what that does to the curve shape and differentials over weeks.
- Third-order (if you can): what the market will over- or under-react to, based on positioning in the brief.
- What changes my mind: the two data points that would confirm or refute the story.
- Trade: pick the instrument that isolates your view (spread, crack, EFS, freight) and state the size in risk terms, the stop, and the horizon. Say explicitly why you would not simply go outright.
**Pushback:**
- "The market has already moved $2 on this. What's the trade now?" (Judge whether the move is complete relative to the barrel impact; often the second-order trade — spreads or differentials — has not moved yet.)
- "What would make this a non-event in a week?" (Name the reversal condition.)
**Red flags:** Repeats the headline without a mechanism, or gives a trade with no risk definition.

### Q17. TEMPLATED — The Glencore item in this morning's brief is "{{glencore_news}}". What does it mean for the business, and would you have made the same decision?
**Difficulty:** 2
**Model answer:**
- Classify: Marketing (trading), Industrial (copper, cobalt, coal, zinc, nickel, ferroalloys), corporate (M&A, capital returns, coal strategy), or compliance/legal.
- Quantify what you can: production guidance, volumes, EBIT sensitivity (e.g. how much a $X/t move in copper or coal changes Industrial earnings — the annual report publishes sensitivities; check the latest).
- Strategic read: how the item fits Glencore's stated strategy — integrated Marketing plus Industrial, portfolio shift toward transition metals, coal cash generation and the debate over keeping it, capital returns, and the remediation of the 2022 settlements.
- Your judgement: agree or disagree, with one reason, and what you would watch to know if it worked. Show you can be respectful and independent at the same time.
- Trading angle: does it change any flows Marketing handles (captive tonnes, new offtake, a mine closure removing supply from the market)?
- If the item is negative (accident, litigation, guidance cut), lead with the human or compliance dimension before the numbers.
**Pushback:**
- "How does this compare with what Trafigura/Vitol would do?" (They don't own mines at scale — Glencore's differentiator is the integration; be able to say why that is an advantage and a burden.)
- "Do you know what our Marketing EBIT guidance range is?" (Check the latest results; know the long-term range and where the last year printed.)
**Red flags:** Has not read the brief, or flatters the company without an opinion.

### Q18. TEMPLATED — Copper is at {{copper_flat}} and the metals story of the day is "{{top_metals_story}}". Is the story already in the price?
**Difficulty:** 3
**Model answer:**
- Start with what "in the price" means: has the flat price, the spread structure (cash-3M), the physical premium and the SHFE-LME arb all moved consistently with the story? If only flat price moved, the physical market has not confirmed.
- Quantify the story in tonnes per year and against a ~26-27 million t refined market; a mine outage of 100 kt/yr is ~0.4% of supply — meaningful only if the market is already tight.
- Check positioning from the brief (COT, open interest, options skew); a story that the crowd is already long is more likely to fade.
- View: priced / not priced / over-priced, with the specific indicator that persuades you.
- What changes my mind: the next stock and premium prints, Chinese import data, and whether the story develops (strike settled, tariff enacted) or fades.
- Expression: if not priced, long the spread or a call spread; if over-priced, sell the rally via put spreads or short cash-3M once the squeeze risk is understood; physically, adjust the timing of hedges on quotational periods.
**Pushback:**
- "Give me a number: how much of a $X move is the story worth?" (Use elasticity thinking: what stock draw does it imply, and what backwardation does that stock level historically carry?)
- "Why are you looking at LME when the marginal buyer is Chinese?" (SHFE and Yangshan premium are the primary signals; LME is the hedge venue.)
**Red flags:** No reference to spreads, stocks or premiums — only flat price.

### Q19. TEMPLATED — Brent is at {{brent_flat}}. Is the market too long or too short, and how does that change how you'd trade the next two weeks?
**Difficulty:** 3
**Model answer:**
- Positioning evidence: managed-money net length from the COT (ICE and CFTC) as a percentile of its history, open interest changes, options skew (put vs call implied vol), and the M1-M2 spread relative to inventories (spec-driven backwardation without stock draws is a warning).
- Interpretation: extreme length means the market is vulnerable to bad news and rallies are sold; extreme shorts mean squeezes on any supply headline. Positioning tells you about the path and asymmetry, not the destination.
- Combine with fundamentals from the brief: if fundamentals are bullish and positioning is short, that is the best set-up; bullish fundamentals with record length is a "right but late" set-up.
- View: "The market is [long/short/neutral]; I'd expect [asymmetric move] over two weeks, and I'd position for it with [instrument]".
- What changes my mind: a flush in open interest, a change in skew, or a fundamental shock that overrides positioning.
- Expression: options work best for asymmetric positioning trades — buy the cheap tail (calls if the market is short and skew favours puts); or trade the front spread which is where positioning shows first. Size small: positioning trades have a bad hit rate but good payoff.
**Pushback:**
- "COT data is a week old. How useful is it?" (Directionally useful; supplement with open interest, spread behaviour and the options market for real-time reads.)
- "Would you fade a crowded long ahead of an OPEC+ meeting?" (Depends on the expected decision and its asymmetry; explain the risk of being short into a cut.)
**Red flags:** No source for the positioning claim, or equates "everyone is long" with "price must fall".

### Q20. Tell me something the market is wrong about right now, and how you'd put $10 million of VaR behind it.
**Difficulty:** 3
**Model answer:**
- Pick one idea from the brief and state it as a mispricing, not a prediction: "The curve implies X, I think Y because Z". The best answers are about a spread, differential or arb where the mechanism is checkable, not a flat-price call.
- Give the evidence: two or three facts (stocks, flows, policy) and one piece of contrarian logic (why the market is discounting it — positioning, a consensus narrative, a lag in data).
- What changes your mind: a specific print or event with a threshold and a date.
- Sizing to $10m VaR: pick the instrument, its daily vol, and back out the size (e.g. a spread with $0.15/bbl daily vol at 95% → 1.65 × 0.15 = ~$0.25/bbl VaR per bbl; $10m / $0.25 ≈ 40 million bbl-equivalents... which is too big for the market, so cap by liquidity and say so). Show you know limits bind before VaR does.
- Stop and target: where you exit for a loss, where you take profit, and the time horizon.
- Be willing to be challenged and to update in real time; the interviewer wants to see you think, not defend a script. If they demolish your view, say what part survives.
**Pushback:**
- "I'm the other side of your trade. Sell me your reasons." (Keep it to three; if you add a fourth you sound unsure.)
- "Your stop is hit on day two. What now?" (Take the loss, re-examine the thesis, do not average down; explain what would make you re-enter.)
**Red flags:** Picks a consensus view ("oil is going higher because of demand") or cannot size the trade.

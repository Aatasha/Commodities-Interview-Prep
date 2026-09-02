# Technical Question Bank

How to use: work through these in order (easy to hard) and answer out loud before reading the model answer. The model answer is the shape of a strong graduate/trainee response at Glencore, Trafigura, Vitol, Mercuria or Gunvor: it leads with the mechanism, gives a number, and stops. The "Pushback" bullets are the follow-ups a desk head will throw at you; if you cannot survive them you do not know the topic yet. Numbers in these answers are illustrative orders of magnitude; anything that moves (spreads, TCs, freight rates, sanction regimes) should be refreshed from the latest brief in `briefs/` before an interview. Conventions used throughout: 1 ICE Brent lot = 1,000 bbl; 1 LME copper lot = 25 t; ~7.33 bbl/t for Brent-type crude; 1 bbl of oil ≈ 5.8 MMBtu; 1 MWh = 3.412 MMBtu.

Coverage:
- Contango vs backwardation, full carry (storage + financing + insurance), why backwardation signals tightness
- Hedging a physical cargo with futures: lots, basis risk, EFPs, pricing periods
- Brent vs WTI drivers; Dated Brent vs futures (CFDs, DFLs); Brent-Dubai EFS and sweet/sour
- Crack spreads (3-2-1, gasoline vs distillate) and refinery configuration
- Freight: VLCC/Suezmax/Aframax, Worldscale, tonne-miles, sanctions and voyage length
- Arbitrage economics and landed cost
- Options for a trader: delta, puts vs futures, volatility
- LME structure: 3M, prompt dates, cash-3M, tom-next, warrants, warehouse queues, squeezes
- How a trading house makes money; physical vs paper P&L; books and P&L attribution
- Prepayment and offtake deals; why miners sell to traders
- Copper/cobalt supply chain: DRC, China refining, TC/RCs and payables
- LNG pricing: Henry Hub-linked, oil-indexed, TTF/JKM
- Coal benchmarks: Newcastle 6,000 vs 5,500 NAR, API2, API4
- VaR and position limits
- Why time spreads matter more than flat price to a physical trader

---

### Q1. Explain contango and backwardation, and what "full carry" means.
**Difficulty:** 1
**Model answer:**
- Contango: later-dated prices above nearer ones (M2 > M1). Backwardation: nearer prices above later ones (M1 > M2). Describe the curve by the M1-M2 spread in $/bbl or $/t, not just the label.
- Carry is what it costs to hold a barrel for a month: storage + financing + insurance (+ small losses/handling).
- Illustrative Brent numbers: onshore tank $0.40-0.50/bbl/month; financing $80/bbl × 6% / 12 ≈ $0.40; insurance and losses ~$0.03-0.05. Full carry ≈ $0.85-0.95/bbl/month.
- If the contango is wider than full carry, the storage trade pays: buy prompt, sell deferred futures, put oil in tank, deliver against the short. Arbitrage pulls the spread back toward full carry, so full carry is the practical ceiling on contango.
- There is no equivalent floor on backwardation because you cannot borrow physical barrels from the future; backwardation can be as steep as the shortage is severe.
- For LME metals the same logic: cash-3M contango caps at rent + finance + insurance (roughly $30-60/t on copper over 3 months depending on rates); backwardation is uncapped.
**Pushback:**
- "Storage costs $0.45 but the M1-M2 contango is only $0.50. Do you put the trade on?" (Only if financing + insurance fit in the remaining $0.05 — they don't at any normal rate. Ask what your cost of funds is.)
- "Why do we sometimes see contango wider than full carry?" (Tank tops: no free capacity at the quoted rate; the marginal storage is floating storage or nothing, and the spread has to blow out to ration it — e.g. spring 2020.)
**Red flags:** Confuses the two terms, or says contango is "normal" without linking it to carry cost.

### Q2. Why does backwardation signal a tight market?
**Difficulty:** 1
**Model answer:**
- Backwardation means the market pays a premium for barrels now over barrels later. Rational holders of inventory only sell at a discount to the future if they have to, so a persistent backwardation means prompt supply is scarce relative to prompt demand.
- Mechanically: refiners bid up prompt cargoes to keep running; nobody wants to store because holding inventory into a backwardated curve loses the spread every month (negative roll yield).
- Inventories therefore fall in backwardation and build in contango — the curve and the stock level are the same signal seen twice. Watch OECD commercial stocks, Cushing, ARA and Singapore product stocks against the spread.
- A very steep front spread (e.g. Brent M1-M2 above $1.50-2.00) usually points to a physical squeeze, outage, or a dislocation (sanctions, Hormuz risk) rather than a balanced market.
- Backwardation also discourages hedging by producers (they sell forward at lower prices) and encourages consumers to hedge, which feeds back into the shape.
- Caveat: a spread can be technical — expiry positioning, a squeeze in a deliverable grade, an index roll — so confirm with physical differentials (Dated vs futures, Forties differential, WTI Midland vs Cushing).
**Pushback:**
- "Give me a case where the curve is backwardated but the physical market is weak." (Paper-driven backwardation: spec length in front months while Dated differentials and North Sea diffs are negative; the curve then flattens rather than the physical firming.)
- "What inventory number would you look at to confirm?" (Cushing for WTI; ARA product stocks and Singapore onshore for products; OECD total commercial; and floating storage counts.)
**Red flags:** "Backwardation means prices are going up." It says nothing directly about the forward flat price level.

### Q3. How does a physical trading house actually make money? Is it a directional bet on price?
**Difficulty:** 1
**Model answer:**
- No. Flat price is hedged as a matter of policy; a trading house earns a margin on moving, storing, transforming and financing commodities. Gross margins are thin (order of $1-2/bbl on oil, a few $/t on coal or concentrates) so the business is volume times reliability.
- Sources of margin: (1) geographic arbitrage — buy where it's cheap, ship to where it's dear, capture landed-cost gap net of freight; (2) time arbitrage — store in contango, deliver later; (3) quality arbitrage — blend off-spec or heavy streams into a spec that sells at a premium; (4) embedded optionality — delivery windows, quantity tolerances (±5-10%), origin/destination options in contracts; (5) financing — prepayments and inventory finance at a spread over the house's funding cost; (6) logistics — controlling terminals, tanks, rail, vessels; (7) for Glencore, industrial assets that provide captive flow to Marketing.
- Paper P&L is the daily mark-to-market on futures/swaps/options; physical P&L crystallises when the cargo is priced and delivered. What matters is the combined book: after hedging, the trader is long or short differentials, time spreads, cracks, freight and FX, not flat price.
- Information advantage is real: seeing physical flows, nomination patterns and who is bidding tells you which differentials are moving before the screen does.
- Glencore frames this as "Marketing" EBIT: a guided long-term range that is meant to be repeatable across price cycles (check the latest results for the current range and actuals).
**Pushback:**
- "If flat price is hedged, why did trading houses make record money in 2022?" (Volatility widens every spread they are exposed to — time spreads, freight, cracks, gas-oil, regional dislocations — and dislocation creates arbs; they are long volatility in structure, not in flat price.)
- "Name a risk that stays even after you hedge flat price." (Basis: the physical prices off Dated or a regional index, the hedge is a futures month; plus counterparty, performance and operational risk.)
**Red flags:** Describes the job as "buying low and selling high" with no mention of spreads, logistics or hedging.

### Q4. What drives the Brent-WTI spread?
**Difficulty:** 1
**Model answer:**
- Quality: WTI is ~40 API and ~0.3% sulphur, slightly lighter and sweeter than Brent (~38 API, ~0.4% S), so on quality alone WTI should trade at a small premium. It normally trades at a discount, so the spread is mostly location.
- Location/logistics: WTI is priced at Cushing, Oklahoma, landlocked; Brent is seaborne. The spread is the cost of getting a barrel from Cushing to the water and across the Atlantic: pipeline tariff to the Gulf Coast (~$1-2/bbl), terminal fees, and Aframax/Suezmax freight USGC-Europe (~$2-4/bbl depending on the tanker market).
- US export capacity: since the 2015 export ban repeal, Corpus Christi, Houston and LOOP set the arb. When export docks are constrained or Cushing stocks build toward tank tops, WTI has to discount to clear; in April 2020 the front-month went negative.
- Cushing stocks and pipeline flows: low Cushing inventories (operational minimum around 20 mb) can squeeze the WTI front spread and narrow Brent-WTI; builds do the opposite.
- Structural: WTI Midland is now a deliverable grade in Dated Brent (since June 2023), so the front of the two markets is more tightly linked, and the spread tends to sit near the USGC-to-Europe freight-plus-tariff cost.
- Short-run drivers: hurricanes (USGC exports stop, WTI weakens vs Brent), refinery turnarounds, freight spikes, and Atlantic basin balances.
**Pushback:**
- "If Brent-WTI is $4 and freight USGC-Rotterdam is $2.50, what do you do?" (Buy WTI at Houston, sell Brent-linked cargo CIF Europe, fix an Aframax; check the differential of WTI Houston vs Cushing first — the arb is against Houston, not Cushing.)
- "Why did WTI go negative in April 2020 but Brent did not?" (WTI is physically delivered at Cushing which was near tank tops; longs with no storage had to pay to get out; Brent is cash-settled against a seaborne market with floating storage as an outlet.)
**Red flags:** Says WTI is "worse quality" than Brent, or cannot name Cushing.

### Q5. What is a 3-2-1 crack spread, and how does refinery configuration change which crack a refiner cares about?
**Difficulty:** 2
**Model answer:**
- A crack spread is the refining margin proxy: product value minus crude cost. The 3-2-1 assumes 3 bbl of crude yield 2 bbl gasoline and 1 bbl distillate: crack = (2 × RBOB + 1 × ULSD − 3 × WTI) / 3, with products converted from $/gal to $/bbl by × 42.
- Worked example: RBOB $2.45/gal = $102.90/bbl, ULSD $2.60/gal = $109.20/bbl, WTI $75: (205.80 + 109.20 − 225) / 3 = $30/bbl.
- Europe typically quotes a 6-3-2-1 or single-product cracks against Brent (gasoil crack, gasoline crack, HSFO crack); Asia against Dubai.
- Configuration: a hydroskimmer (distillation + reforming) makes a lot of fuel oil and lives or dies on the light-heavy differential; a cracking refinery (FCC/hydrocracker) upgrades VGO into gasoline/diesel; a coking refinery converts residue too and makes money running heavy sour crude when the heavy discount is wide. Nelson Complexity Index captures this (simple ~2-4, USGC cokers 10+).
- Gasoline vs distillate: FCC-heavy refineries (US) are gasoline-weighted; hydrocracker-heavy (Europe, Asia, Middle East new builds) are distillate-weighted. Diesel cracks are structurally supported by trucking, industry and jet substitution; gasoline is seasonal (summer driving, RVP switch).
- A trader uses cracks to decide whether to run crude, to time storage of products, and to read demand: cracks up while flat price is flat means product tightness, not crude tightness.
**Pushback:**
- "Distillate crack is $35 and gasoline crack is $10. What does a simple refiner do?" (Maximise distillate: lower FCC severity, run heavier cut points, buy diesel-rich crudes; a hydroskimmer cannot re-weight much and should check whether its margin is even positive after energy costs.)
- "What happens to cracks if OPEC+ cuts medium sour supply?" (Heavy-light narrows, coker economics fall, sour crudes firm vs Brent; product cracks depend on whether refiners cut runs — if they do, cracks widen.)
**Red flags:** Cannot do the $/gal to $/bbl conversion, or thinks the crack is a single product price.

### Q6. You have bought a 1 million barrel Brent-related cargo FOB, pricing over five days around bill of lading. How do you hedge it, and what risks remain?
**Difficulty:** 2
**Model answer:**
- Size: 1,000,000 bbl / 1,000 bbl per lot = 1,000 ICE Brent lots. Sell 1,000 lots of the futures month that best matches the physical pricing period (Dated cargoes loading in a given month usually price off the front or second-month futures via the CFD chain).
- Timing: the physical prices as an average over five quotes, so you sell 200 lots per day over the pricing window (or use a swap/averaging instrument) to match the average. Hedging all at once leaves you exposed to the average vs a point price.
- Basis risk: the cargo prices off Dated Brent plus/minus a grade differential; the hedge is a futures month. The Dated-to-futures gap (DFL) and the grade diff can move independently. Cover with CFDs (Dated vs forward BFOE) or a DFL swap if you want to lock the full chain.
- Lift the hedge when the cargo is sold: buy back the futures as the sale prices, or do an EFP — exchange your futures for the physical leg at an agreed price via the exchange, so the counterparty takes the futures position and you avoid execution slippage in the screen.
- Residual risks: quantity (B/L outturn vs nominated, ±0.5% or more), timing (loading delays shift the pricing window), quality (assay), counterparty and performance, demurrage, freight if you are CIF, FX if selling in a non-USD market, and margin calls on the futures while the physical is unpriced.
- Explain the sign: the hedged position is now long basis; if Dated strengthens vs futures you make money on the physical relative to the hedge.
**Pushback:**
- "The buyer wants to price on a Dubai basis. Now what?" (Add a Brent-Dubai EFS to convert the Brent hedge into a Dubai exposure, and size on the same barrels; you now carry EFS risk instead of Dubai flat price.)
- "You are short 1,000 lots and Brent rallies $5 before you sell the cargo. How much cash do you need?" ($5 × 1,000 × 1,000 = $5m variation margin, funded from the treasury line even though the physical is worth $5m more; unrealised physical gain doesn't pay the margin call.)
**Red flags:** Wrong lot count, or thinks hedging removes all risk.

### Q7. Walk me through crude tanker classes, Worldscale, and why sanctions lengthen voyages.
**Difficulty:** 2
**Model answer:**
- Sizes: VLCC ~300,000 dwt, ~2 million bbl; Suezmax ~150-160,000 dwt, ~1 million bbl; Aframax ~80-120,000 dwt, ~600-750k bbl; for products, LR2 (~90k dwt), LR1 (~60-75k dwt), MR (~38-50k dwt, ~300k bbl of diesel). Panamax/Capesize are dry bulk (coal, iron ore).
- Worldscale: a published flat rate in $/t for each route on a notional standard vessel, recalculated annually from bunker prices and port costs. Fixtures are quoted as a percentage: WS 65 on a $18/t flat rate = $11.70/t ≈ $1.60/bbl for crude (÷7.33). WS 100 = the flat rate.
- Time charter equivalent (TCE) converts a voyage into $/day so owners can compare routes; a $45,000/day VLCC on a 60-day round trip with 2 mb on board is ~$1.35/bbl hire before bunkers.
- Tonne-miles = cargo tonnes × distance sailed: the true measure of tanker demand. Same barrels, longer route = more ships tied up.
- Sanctions: Russian Urals that used to sail Primorsk-Rotterdam (~5 days) now sails to India or China (~25-35 days) — the same volume needs 5-6× the ship-days. Add ship-to-ship transfers, a shadow fleet that Western charterers cannot use, and Red Sea/Cape diversions adding 10-14 days on Asia-Europe, and the effective fleet shrinks even though no ship is lost.
- Effect on trading: freight becomes a bigger share of landed cost, regional differentials widen, and the arb window opens or closes on freight moves rather than flat price.
**Pushback:**
- "Freight rates double. Who wins between a producer selling FOB and one selling CIF?" (FOB seller is unaffected on the fixture but sees weaker FOB netbacks as buyers subtract freight; CIF seller with unfixed freight loses; a trader with time-chartered tonnage is long freight and gains.)
- "Why do product tankers sometimes earn more than VLCCs?" (Different fleets, different demand: refinery dislocation, e.g. the EU product ban on Russia, drove MR/LR demand and tonne-miles while crude VLCC demand lagged.)
**Red flags:** Cannot size a VLCC in barrels, or thinks Worldscale is a $/bbl figure.

### Q8. Show me the landed-cost calculation for an arbitrage and tell me when the arb is "open".
**Difficulty:** 2
**Model answer:**
- Landed cost at destination = FOB price + freight + insurance + financing + losses/handling + port and inspection fees (+ duty if any). Compare against the delivered price (CIF/DAP) you can sell at, or the local index (e.g. CIF ARA, CFR South China).
- Diesel ARA to West Africa, $/t: FOB $720; MR freight $45; insurance ~$1; financing 25 days × 6% on $720 = $3; in-transit and outturn losses 0.3% ≈ $2.2; port/inspection $3. Landed ≈ $774/t. If delivered West Africa trades above that, the arb is open; below, it is closed.
- Convert to $/bbl by dividing by bbl/t: diesel ~7.45 bbl/t, so $774/t ≈ $104/bbl.
- Freight is the swing item; it must be quoted for the right ship size, route, and laycan, plus demurrage exposure. Financing depends on days from payment to receipt (letter of credit terms), not just voyage days.
- Timing risk: the arb you see today closes if the destination price falls while the ship is at sea; hedge each leg (sell destination index swap, buy origin index swap, or fix the spread) so you are left with the locked margin plus basis.
- "Arb open" on the screen is often a mirage: check whether the delivered price is for the spec you have (sulphur, cetane, density), whether tank space and berths exist, and whether the counterparty can pay.
**Pushback:**
- "The arb shows $8/t. Do you do it?" (Only if the risk-adjusted margin covers demurrage variance, hedge slippage and credit; $8/t on a 37,000 t cargo is $296k gross — small against a two-day demurrage bill at $30k/day.)
- "What losses do you assume on crude vs products?" (Crude ~0.3-0.5% total for load/discharge and in-transit; clean products lower but with contamination risk; LNG has boil-off ~0.1%/day.)
**Red flags:** Forgets financing or losses, or compares FOB to CIF without freight.

### Q9. What are the main seaborne thermal coal benchmarks and how do they relate?
**Difficulty:** 2
**Model answer:**
- Newcastle 6,000 kcal/kg NAR (globalCOAL NEWC / ICE futures): the high-CV Pacific reference, historically bought by Japan, Korea, Taiwan.
- Newcastle 5,500 NAR (Argus/McCloskey): lower-CV Australian coal into China and India; trades at a discount that is usually wider than the energy adjustment alone (5,500/6,000 = 91.7%) because of higher ash and buyer mix.
- API2: CIF ARA 6,000 NAR — the Atlantic/European delivered reference; API4: FOB Richards Bay 6,000 NAR — South African export reference. API2 minus API4 should approximate Richards Bay to ARA freight (Capesize/Panamax, tens of $/t); if it exceeds freight the South Africa-to-Europe arb is open.
- Indonesian coal is priced by ICI indices on a GAR basis (e.g. ICI4 4,200 GAR); GAR (gross as received) is higher than NAR (net) by the latent heat of moisture, roughly 200-300 kcal for high-moisture Indonesian product. Always check the basis before comparing.
- Glencore is one of the largest seaborne thermal coal exporters (Australia, Colombia, South Africa) so pricing, quality blending (mixing low-ash and high-ash to hit a spec) and destination optionality are core skills.
- Drivers: Asian power demand and heat waves, hydro output in China, gas-to-coal switching in Europe (compare API2 in $/MWh against TTF and carbon), Chinese domestic production and import policy, Indian monsoon and stock levels.
**Pushback:**
- "NEWC is $130 and 5,500 NAR is $90. Blend or not?" (Energy-adjusted, 5,500 should be ~$119; at $90 the low-CV product is cheap on a per-GJ basis — blend it with higher-CV coal if the ash/sulphur spec tolerates it, and sell as a 5,800-6,000 product.)
- "How would you compare coal with gas for a European utility?" (Convert both to $/MWh of fuel: coal at 6,000 NAR ≈ 6.98 MWh/t, so API2 $100/t ≈ $14.3/MWh thermal; adjust for plant efficiency (coal ~38%, CCGT ~55%) and carbon (coal ~0.9 t CO2/MWh vs ~0.35 for gas).)
**Red flags:** Doesn't know NAR vs GAR, or treats all "Newcastle" as one price.

### Q10. How is LNG priced? Explain Henry Hub-linked, oil-indexed, and hub-indexed contracts.
**Difficulty:** 2
**Model answer:**
- US export (Henry Hub-linked): FOB price = 115% × Henry Hub + a fixed liquefaction fee (typically $2.25-3.50/MMBtu). The 15% uplift covers gas used as fuel in liquefaction. The fee is take-or-pay: the offtaker pays it whether or not it lifts, so the variable cost of lifting is only 1.15 × HH plus shipping.
- Example: HH $3.00 → 3.45 + $2.50 fee = $5.95 FOB; add ~$1.50 shipping to Europe and ~$0.30 regas → ~$7.75 landed; against TTF at $11 that's a ~$3.25 margin. A standard 174,000 m³ cargo is ~3.5-3.6 TBtu, so that margin is ~$11-12m per cargo.
- Oil-indexed (legacy Asian long-term): price = slope × Brent (or JCC) + constant, with a 3-6 month lag; slope 11-14%, e.g. 12% × $80 = $9.60/MMBtu. Often with S-curves that flatten at extremes.
- Hub-indexed: TTF (EUR/MWh; convert × EURUSD ÷ 3.412 to $/MMBtu) for Europe, JKM ($/MMBtu, Platts) for Northeast Asia spot, NBP in the UK.
- Cargo direction: a flexible-destination cargo goes to the higher netback; JKM minus TTF has to exceed the extra shipping and canal cost to pull cargoes to Asia. Cancellations of US cargoes happen when 1.15 × HH + variable shipping exceeds the destination price (fee is sunk).
- Trading houses earn on destination flexibility, shipping optionality, and the spread between contract formulae and spot.
**Pushback:**
- "TTF drops below HH-linked cost. What does the offtaker do?" (Cancel the lift and eat the fixed fee; the loss is the fee, not the full price. Compare to selling the cargo at a loss including fee.)
- "Why did the oil-indexation link break down?" (US flexible supply and hub liquidity; oil-linked prices can be far above or below spot gas, so buyers renegotiate; still relevant in Asia for long-term security-of-supply contracts.)
**Red flags:** Cannot convert TTF into $/MMBtu, or doesn't know the 115% mechanic.

### Q11. Describe the copper and cobalt supply chain from the DRC to a cathode buyer, and what TC/RCs and payables are.
**Difficulty:** 2
**Model answer:**
- The DRC (Copperbelt: Kolwezi, Lubumbashi) is the world's largest cobalt producer (well over half of mined supply) and a top-two copper producer; Glencore's KCC and Mutanda are major assets. Cobalt is largely a by-product of copper there.
- Output leaves as copper cathode (from SX-EW) or as copper-cobalt hydroxide/concentrate, trucked via Zambia to Durban/Dar es Salaam/Walvis Bay/Lobito (rail), then shipped mostly to China, which refines the majority of the world's cobalt and a large share of copper.
- Copper concentrate (~25-30% Cu) is sold to smelters; the miner pays TC (treatment charge, $/dmt of concentrate) and RC (refining charge, c/lb of payable copper) and gets paid on ~96.5% of contained copper (a 1-unit deduction or fixed payable), plus/minus penalties (arsenic) and credits (gold, silver).
- TC/RCs move with the concentrate balance: when new smelting capacity outruns mine supply, smelters cut charges to win feed (benchmark TCs fell sharply in the mid-2020s toward historic lows and spot went near zero or negative; check the latest brief). Low TC/RCs = miners win, smelters squeezed.
- Cobalt hydroxide is priced as a payable percentage of the metal reference price (Fastmarkets standard-grade cobalt), historically anywhere from ~50% to 90%+ depending on the balance; DRC export policy (bans/quotas) has been used to manage oversupply — check current status.
- Risks a trader manages: logistics and border delays, ESG/artisanal-mining provenance, Chinese import policy, credit, and the mismatch between LME copper hedges and physical payable tonnes.
**Pushback:**
- "How many LME lots do you hedge for 12,000 t of concentrate at 28% Cu?" (12,000 × 0.28 × 0.965 = 3,242 t payable → ~130 lots; and note the quotational period usually sits months after delivery.)
- "Why would a Chinese smelter accept a zero TC?" (Marginal economics of by-product credits, sulphuric acid sales, subsidies and the need to keep the furnace running; also price participation clauses.)
**Red flags:** Thinks cobalt is mined on its own, or cannot explain who pays TC/RCs.

### Q12. What is a prepayment or offtake deal, and why do producers sell to traders instead of marketing themselves?
**Difficulty:** 2
**Model answer:**
- Prepayment: the trader advances cash (tens of millions to billions of dollars) to a producer, repaid in physical deliveries over an agreed period at a market-linked price minus a discount. It is a loan secured on future flow and priced to cover the house's funding cost plus a risk margin.
- Offtake: a commitment to buy a defined volume (e.g. 100% of a mine's cobalt hydroxide for five years) at index-linked terms; often paired with prepayment, streaming, or equity.
- Producer's benefits: cheaper and faster than bank debt for a mid-tier or frontier miner; no equity dilution; guaranteed buyer; access to the trader's blending, logistics, working capital and credit; a marketing department they don't need to build.
- Trader's benefits: captive flow to feed the book and its logistics; embedded optionality (delivery timing, destination, quality); financing margin; information from seeing the producer's output.
- Risks: performance (the mine underdelivers), political/sanctions, counterparty credit, price (mitigated by index pricing and hedging the future deliveries as they price), and reputational — including bribery risk in high-risk jurisdictions, which is why compliance signs every deal now.
- Mitigants: security over assets, accounts and export licences, syndication with banks, insurance (political risk, credit), volume flexibility, cross-default clauses.
**Pushback:**
- "Price halves after you've prepaid $200m. Are you worse off?" (Yes on the tenor: you receive twice as many tonnes/barrels over more time to repay the same dollars, extending exposure; hedges on scheduled deliveries protect the priced volume but not the extension.)
- "Why did banks pull back from this business, leaving it to traders?" (Basel capital rules, reputational risk, and the need to physically monetise collateral; traders can take delivery and sell the product, banks can't.)
**Red flags:** Describes it as charity to the miner, or misses that it's secured lending with physical repayment.

### Q13. Explain delta, and when a trader would buy puts rather than sell futures to protect a long physical position.
**Difficulty:** 2
**Model answer:**
- Delta is the option's price sensitivity to the underlying: a 0.30-delta put loses $0.30 per $1 rise in the future. It's also a rough probability of finishing in the money. To delta-hedge a long cargo with puts you'd need 1/delta as many contracts — with 0.50-delta puts, 2,000 lots to cover 1 million bbl, whereas 1,000 futures give a full hedge.
- Selling futures locks the price: no upside, no downside, daily variation margin, and basis risk vs the physical index.
- Buying puts sets a floor and keeps the upside; the cost is the premium (time value decays) and the risk is paying for protection you don't use. Cash outlay is capped at the premium, so no margin calls — attractive when treasury lines are tight or when the physical hasn't priced yet.
- Use puts when: you have a view that the market rallies but must protect against a crash; when the exposure itself is uncertain (a cargo that may or may not load, a tender you may not win); when volatility is cheap relative to your view of realised moves.
- Volatility: implied vol is the market price of protection; if implied is high (post-shock) buying puts is expensive — consider a put spread or collar (sell a call to fund the put, giving up upside above the strike).
- A physical trader's own book contains optionality: storage is a call on the time spread, a blending facility is a call on quality differentials, a flexible-destination cargo is an option on regional spreads.
**Pushback:**
- "Vol is 45%. Do you still buy the put?" (Compare implied with expected realised vol; if you think the market is going to sit still, a collar or simply selling futures is cheaper. Also check skew — puts are usually expensive relative to calls in oil.)
- "Your puts are 0.30 delta and the market drops $10. Are you hedged now?" (Delta has risen toward 0.70-0.80; the put now covers most of the move but you were under-hedged on the first leg down — that's gamma. You could buy fewer futures back as delta rises.)
**Red flags:** Can't explain delta numerically, or says options are "safer" without mentioning premium.

### Q14. What is VaR, how is it calculated, and how do desks use position limits?
**Difficulty:** 2
**Model answer:**
- Value at Risk: the loss over a holding period that you expect not to exceed with a given confidence — e.g. a 1-day 95% VaR of $20m means a 1-in-20-day loss should not exceed $20m.
- Parametric shortcut: VaR = position value × daily volatility × z (1.65 at 95%, 2.33 at 99%). A $100m net exposure with 2% daily vol at 99% → $100m × 0.02 × 2.33 = $4.66m. Real desks use historical simulation or Monte Carlo across all risk factors (flat price, spreads, cracks, freight, FX) with correlations.
- Limits stack: VaR limit per book and firm; net and gross position limits by commodity and tenor (e.g. max 5,000 lots net Brent, max 2,000 in any single month); stop-loss triggers; Greek limits for options (delta, gamma, vega); concentration and single-counterparty credit limits; liquidity/tenor limits.
- Weaknesses: VaR says nothing about the size of tail losses beyond the threshold; correlations break in stress (2020, 2022); a physical cargo cannot be liquidated in one day, so 1-day VaR understates physical liquidity risk. Use stress tests and scenario analysis alongside it.
- Glencore, like the other houses, publishes a 1-day 95% VaR for its Marketing book in the annual report (historically a modest two-digit $m figure — check the latest). Trading houses also monitor basis risk explicitly because VaR built on futures curves can miss it.
- What a trainee should show: an instinct for what limits are for — protecting the franchise, not just the P&L — and awareness that a breach needs escalation, not silence.
**Pushback:**
- "Your VaR is within limit but you hold 30 cargoes at sea. Are you safe?" (No: operational, counterparty, sanctions and liquidity risk aren't in the VaR number; and if all 30 price on the same index the concentration is enormous.)
- "Why 95% and not 99%?" (95% gives more exceedances to backtest against — 12-13 a year — so the model is testable; 99% tail estimates are noisier. Regulators prefer 99%; traders manage to both.)
**Red flags:** Says VaR is the "maximum loss".

### Q15. What is a "book" on a trading desk, and how does daily P&L attribution work?
**Difficulty:** 2
**Model answer:**
- A book is the set of positions a trader or desk is accountable for: physical purchase and sale contracts (priced and unpriced), inventory in tank/on water, futures, swaps, options, freight (chartered vessels, FFAs), and FX, valued daily as one P&L.
- Everything is marked to market: physical contracts against the relevant forward curve or index (Dated, Platts assessments, LME), inventory at market, paper at settlement. Realised P&L crystallises when cargoes price and settle; unrealised is the daily mark change.
- P&L attribution ("explain") splits the day's move into risk factors: flat price (should be near zero if hedged), time spreads/structure, basis (physical index vs hedge instrument), quality differentials, cracks, freight, FX, financing/carry cost accrual, option Greeks (theta, vega), and "new deals" (day-one margin on a fresh trade).
- Residual/unexplained P&L is the red flag: it usually means a mis-marked contract, wrong quantity, a hedge in the wrong month, or a demurrage claim nobody booked.
- The desk head reads the explain to check the trader is making money from the intended exposure (e.g. long Dated vs futures) rather than from an unintended one (a flat-price gap because the hedge lagged).
- Middle office owns the marks and the explain; the trader owns the positions; risk sets the limits — separation of duties matters in this industry.
**Pushback:**
- "You show +$2m today but flat price didn't move. Where did it come from?" (Walk the explain: differential move on unpriced cargoes, a spread move on a hedge across months, a freight mark, an FX gain — and be honest if one of them is a mark you changed.)
- "How do you value a cargo that hasn't priced yet?" (At the forward index for its pricing window plus the contractual differential, less freight and costs to the relevant delivery point; unpriced physical is effectively a forward position.)
**Red flags:** Thinks P&L only appears when a cargo is sold.

### Q16. What is the difference between Dated Brent and the ICE Brent future, and how do you get from one to the other?
**Difficulty:** 3
**Model answer:**
- Dated Brent is Platts' assessment of the physical price of a cargo of the cheapest deliverable North Sea grade (Brent, Forties, Oseberg, Ekofisk, Troll, plus WTI Midland since 2023, with quality adjustments) loading in a window roughly 10 days to one month ahead. It is the reference for most of the world's seaborne crude.
- ICE Brent futures are cash-settled against the ICE Brent Index, which is derived from the forward "cash BFOE" market (600,000 bbl forward cargoes for a delivery month). Expiry is the last business day of the second month before delivery.
- The chain: Futures ↔ (EFP) ↔ Forward cash BFOE ↔ (CFD) ↔ Dated Brent. The EFP is the futures-vs-forward-cargo spread; CFDs are weekly swaps of Dated vs the front forward month. A DFL (Dated-to-frontline) swap packages the whole chain: Dated vs front-month futures.
- Roughly: Dated ≈ Futures + EFP + CFD (each signed). When Dated trades at a premium to futures the physical is tight (the DFL is positive/backwardated); when at a discount, prompt cargoes are struggling to clear.
- Why it matters: a trader who hedges a Dated-priced cargo with futures is long or short the DFL; that spread can move $1-3/bbl in weeks. The CFD market is also where physical tightness in the North Sea shows up first.
- Platts' Market on Close window (bids/offers to 16:30 London) is where the assessment is formed; large players' behaviour in the window is scrutinised and has been the subject of manipulation cases.
**Pushback:**
- "What did adding WTI Midland do to the benchmark?" (More deliverable volume, more days when Midland sets the cheapest grade, tighter Brent-WTI linkage, and Dated now partly reflects USGC export economics and freight.)
- "Why is Dated quoted 'loading 10 days to a month ahead' rather than spot?" (Cargo logistics: nomination and vessel fixture need lead time; the window matches how physical North Sea cargoes actually trade.)
**Red flags:** Thinks the Brent future physically delivers, or cannot name a single North Sea grade.

### Q17. What is the Brent-Dubai EFS, and what does a widening EFS tell you?
**Difficulty:** 3
**Model answer:**
- EFS = exchange of futures for swaps: the price at which ICE Brent futures are swapped for a Dubai swap of the same month. Quoted as Brent minus Dubai, it is the market's sweet-versus-sour and Atlantic-versus-Asia spread in one number.
- Dubai is the Middle East medium-sour benchmark: Platts assesses it via partials (25,000 bbl each; 20 partials converge into a physical cargo of Dubai, Oman, Upper Zakum, Al Shaheen or Murban with quality adjustments).
- Uses: Asian refiners hedge Dubai-linked term crude with liquid Brent futures and then convert via EFS; producers of sweet Atlantic crude selling east compare their netback via EFS; traders express a sour-tightness view directly.
- Widening EFS (Brent up vs Dubai): sweet tight or sour loose — e.g. OPEC+ increasing medium-sour supply, weak Chinese teapot demand, or Atlantic disruption (Libya, Nigeria, North Sea maintenance). Narrowing or negative EFS: sour tight — OPEC+ cuts, sanctions on Iran/Russia/Venezuela removing sour barrels, strong complex-refiner demand, or a Hormuz risk premium pricing into Dubai.
- Arb effect: a wide EFS opens the West-to-East arb for Atlantic barrels (WTI, Brent, West African) into Asia because they become competitive with Dubai-linked grades after freight; a narrow EFS shuts it.
- Related: Murban futures (ICE Abu Dhabi) and the Oman contract on DME provide sour futures alternatives; the Dubai-Oman spread and the Brent-Murban spread refine the picture.
**Pushback:**
- "EFS goes negative. What's happening?" (Sour crude pricing above sweet — extreme sour tightness or Middle East supply shock; last seen around 2022 sanctions/OPEC+ cuts and Hormuz scares; complex refiners switch to sweet, coker margins collapse.)
- "How would you position for OPEC+ unwinding its cuts?" (Long EFS — buy Brent, sell Dubai — since the incremental barrels are medium sour; hedge flat price with the same instrument.)
**Red flags:** Cannot say which crude is sweeter, or confuses EFS with EFP.

### Q18. Explain the LME's date structure: cash, 3M, prompt dates, tom-next, and what the cash-3M spread tells you.
**Difficulty:** 3
**Model answer:**
- Unlike a futures exchange with fixed monthly contracts, the LME is a forward market with daily prompt dates out to three months, weekly (Wednesdays) from three to six months, and monthly (third Wednesday) beyond, out to 123 months for copper and aluminium.
- Cash (spot) is T+2. 3M is a rolling date three months forward and is the most liquid, the reference price you see quoted. Tom-next is the one-day spread between tomorrow and the next day; it is the tightest expression of prompt tightness and where squeezes bite.
- Because every date is tradeable, every position eventually rolls through the prompt dates: a trader long 3M who does not want delivery must lend or borrow the position forward (a "carry" trade), paying or receiving the spread.
- Cash-3M spread: contango up to full carry (warehouse rent + financing + insurance; copper rent is a few tens of cents per tonne per day, so three months of full carry is tens of $/t) when metal is abundant; backwardation when nearby metal is scarce relative to warrants available.
- Lot sizes: copper, aluminium, zinc, lead 25 t; nickel 6 t; tin 5 t. Delivery is by warrant on metal in an LME-approved warehouse, and the buyer cannot choose the location.
- Reading the curve: falling on-warrant stocks plus rising cancelled warrants plus a backwardation in tom-next is the classic sign of a squeeze; a flat contango at full carry with rising stocks is a boring, well-supplied market.
**Pushback:**
- "You're long 40 lots of 3M copper and the date is tomorrow. What are your options?" (Sell the position, take delivery of warrants — 1,000 t, paying for metal and rent — or roll: sell tom, buy next (borrow), paying the tom-next spread.)
- "Why does the LME have daily prompts at all?" (It grew out of physical merchant trading: a smelter or fabricator can hedge the exact date it buys or sells metal, which is why physical traders still use it.)
**Red flags:** Treats "3M" as a monthly contract, or doesn't know that LME positions require rolling.

### Q19. How does an LME backwardation squeeze work, what role do warehouse queues play, and what has the exchange done about it?
**Difficulty:** 3
**Model answer:**
- Setup: a participant accumulates a dominant long on a nearby prompt plus control of a large share of warrants. Shorts approaching the date must either deliver metal (which they can't get) or borrow it forward by buying tom-next/cash and selling 3M. With few warrants free, the borrowing cost explodes; tom-next and cash-3M go into steep backwardation and the long collects it.
- Warehouse queues amplify this: metal can be on warrant but stuck behind a load-out queue (Detroit and Vlissingen aluminium queues ran to 12-18 months around 2011-2014), so warrants exist yet metal is not really available. Warehouse rent while queuing was an incentive to keep metal locked in.
- LME responses: load-out rate rules (linked load-in/load-out, queue caps), rent capping while queuing, position reporting, and "lending guidance": a holder of a dominant position (thresholds at 50%, 80%, 90% of warrants/prompt positions) must lend the metal back to the market at capped premiums. Since 2019 the LME also has explicit backwardation limits under the guidance.
- Nickel, March 2022: a huge short (Tsingshan) faced a doubling to over $100,000/t in hours; the LME suspended trading and cancelled trades, later adding daily price limits (15%) and stronger OTC position reporting. Copper in 2021 saw cash-3M backwardation over $1,000/t before the LME intervened.
- Trader's angle: know the warrant holdings, cancelled warrant data and the date your physical hedges roll; never leave a short on a prompt you can't deliver into without a borrow lined up.
- Squeezes are legal only up to a point: exploiting a dominant position is regulated conduct and the lending guidance is a hard rule, not etiquette.
**Pushback:**
- "How would you tell the difference between a real physical shortage and an engineered squeeze?" (Real: premiums for physical delivery (e.g. Shanghai/CIF China premiums, Rotterdam premiums) rising alongside the spread and SHFE stocks falling; engineered: LME spread tight while physical premiums are flat and metal is queuing or sitting off-warrant.)
- "You're the smelter with a short hedge on a cancelled-warrant date. What did you do wrong?" (Hedged into a prompt with no warrant supply plan; should have rolled earlier or hedged against monthly dates.)
**Red flags:** Cannot explain what a warrant is or why a short can't just "buy metal somewhere".

### Q20. Why do physical traders care more about time spreads than flat price?
**Difficulty:** 3
**Model answer:**
- Because flat price is hedged and the spread is not. A hedged cargo, tank of product or warehouse of metal has near-zero flat-price delta but full exposure to the spread between the month it was priced and the month the hedge sits in, plus the cost of rolling.
- Inventory economics are the spread: in a $0.90/bbl/month contango, storing 1 million bbl earns the contango minus carry; in a $0.60 backwardation, holding 2 million bbl for three months costs 2m × 0.60 × 3 = $3.6m regardless of where flat price ends up.
- Roll cost: the futures hedge must be rolled forward each month; in backwardation rolling a short earns the spread, rolling a long pays it. That roll yield is a large part of P&L for anyone holding structural positions.
- Timing optionality: a contract with a delivery window is worth the spread over that window; a cargo you can delay by two weeks in backwardation is worth money — spreads are what you price that optionality against.
- Spreads reveal the physical: M1-M2 and the DFL tell you whether prompt barrels are scarce before stock data prints; a trader who watches the spread trades the tightness, not the headline.
- Sizing: flat-price vol is 2-3% a day on $80 ($2/bbl); a front spread might move $0.20-0.50 a day — so spread positions can be run larger under the same VaR, and are where a physical desk's edge is because they see the flows that drive them.
- The line to remember: flat price is where you get lucky; spreads and differentials are where you get paid.
**Pushback:**
- "Give me a spread trade for a market where OPEC+ has just cut." (Buy M1-M2 or M1-M3: prompt tightens first, while deferred months absorb the cut more slowly; risk is the cut being unwound or demand faltering; express size in $/bbl of spread not in flat-price terms.)
- "If you're so spread-focused, why do houses report big losses in some years?" (Spreads can gap: a contango-to-backwardation flip on a storage book, freight or basis blowouts, counterparty defaults; being spread-heavy doesn't mean low-risk, it means different risk.)
**Red flags:** Says traders make money by "calling the direction of oil".

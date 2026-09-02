# Mental-Maths Question Bank

How to use: a trader will fire these at you mid-conversation and expect an answer in seconds, then a second answer when they change one input. Practise out loud, without a pen, aiming for two significant figures first and the exact number second. Each model answer gives the numeric answer and the mental shortcut a strong candidate uses; the "Pushback" is the twist the trader adds. Memorise the conversion constants below; they are the difference between a fast answer and a blank stare. Numbers in the questions are hypothetical — never quote them as current prices.

Constants to memorise:
- 1 ICE Brent / WTI lot = 1,000 bbl; 1 LME copper lot = 25 t; 1 LME nickel lot = 6 t
- 1 bbl = 42 US gal; 1 m³ = 6.29 bbl; bbl per tonne = 6.29 ÷ specific gravity
- Brent-type crude ≈ 7.33 bbl/t; diesel ≈ 7.45; gasoline ≈ 8.45; fuel oil ≈ 6.35; very heavy crude/residue (SG ≈ 1.0) ≈ 6.29
- 1 bbl of crude ≈ 5.8 MMBtu; 1 MWh = 3.412 MMBtu; 1 t of 6,000 kcal/kg coal ≈ 6.98 MWh thermal
- Wheat: 36.74 bu/t; corn: 39.37 bu/t; soybeans: 36.74 bu/t
- Standard LNG cargo ≈ 174,000 m³ ≈ 3.5-3.6 TBtu; 1 VLCC ≈ 2 million bbl; 1 Aframax ≈ 700,000 bbl; 1 MR ≈ 37,000 t products
- Financing: price × rate × days / 360

Coverage:
- Percentage moves and reverse percentages
- Barrels/tonnes conversions by density; VLCC and cargo sizing
- $/bbl to $/MMBtu; EUR/MWh to $/MMBtu; coal $/t to $/MWh
- Cargo values, futures and LME lot P&L
- Freight: time charter to $/bbl, Worldscale to $/bbl, demurrage
- Financing cost and contango carry decisions
- Crack spread arithmetic, blended weighted average cost, concentrate payable tonnes
- Grain c/bu to $/t
- Quick arithmetic and estimation
- Arb breakeven: diesel Europe to West Africa; LNG US to Europe

---

### Q1. Brent moves from $92.00 to $95.68. What percentage move is that?
**Difficulty:** 1
**Model answer:**
- Answer: +4.0%.
- Shortcut: the move is 3.68. 1% of 92 is 0.92; 4 × 0.92 = 3.68. So exactly 4%.
- General method: divide the move by the starting price; for prices near 100, the move in dollars is roughly the move in percent, then adjust (92 is 8% below 100, so scale the dollar move up by ~8%: 3.68 × 1.087 ≈ 4.0).
- Reverse check: 92 × 1.04 = 95.68. Done.
- On 1,000 lots that move is 1,000 × 1,000 × 3.68 = $3.68m.
**Pushback:**
- "And back from 95.68 to 92 — same percentage?" (No: 3.68 / 95.68 = −3.85%. Percentages aren't symmetric.)
- "What's a 4% move in daily-vol terms if annualised vol is 30%?" (Daily vol ≈ 30% / √252 ≈ 30% / 15.9 ≈ 1.9%; 4% is about a two-sigma day.)
**Red flags:** Starts long division; says "about 4%" without being able to confirm it exactly.

### Q2. A VLCC loads 270,000 tonnes of Brent-type crude. How many barrels is that? And if it were very heavy crude at 6.29 bbl/t?
**Difficulty:** 1
**Model answer:**
- Brent-type at 7.33 bbl/t: 270,000 × 7.33 = 1,979,100 ≈ 1.98 million bbl.
- Shortcut: 270k × 7 = 1.89m; 270k × 0.33 = 89k; total 1.979m. Or: 7.33 ≈ 22/3, so 270k × 22 / 3 = 90k × 22 = 1.98m.
- Heavy at 6.29: 270,000 × 6.29 ≈ 1.70 million bbl (270k × 6 = 1.62m; 270k × 0.29 = 78k; total 1.698m).
- Remember why: bbl/t = 6.29 ÷ SG; Brent SG ≈ 0.858 → 7.33; SG 1.0 → 6.29. Heavier oil = fewer barrels per tonne, so a tonne-based freight rate is more $/bbl for heavy crude.
- Sanity check: a VLCC is "2 million barrels" for light crude; 270 kt is just under a full 300 kt VLCC, so ~2.0m bbl is right.
**Pushback:**
- "Freight is $12/t. What is that per barrel for each grade?" (Brent-type: 12 / 7.33 = $1.64/bbl; heavy: 12 / 6.29 = $1.91/bbl.)
- "The B/L shows 1,950,000 bbl. What's the shortfall in percent?" (1,979,100 − 1,950,000 = 29,100; 29,100 / 1,979,100 ≈ 1.5% — outside a typical 0.5% tolerance, so investigate.)
**Red flags:** Multiplies by 6.29 for Brent, or can't explain where 7.33 comes from.

### Q3. Brent is $87/bbl. What's that in $/MMBtu, and what would a 12%-slope oil-indexed LNG contract pay?
**Difficulty:** 1
**Model answer:**
- $/MMBtu = 87 / 5.8 = $15.00/MMBtu. (5.8 × 15 = 87 exactly.)
- Shortcut: divide by 6 then add 3.5%: 87 / 6 = 14.5; 14.5 × 1.035 ≈ 15.0. Or remember the anchor: $58 = $10/MMBtu, so $87 = 1.5 × 10 = 15.
- Oil-indexed LNG at 12% slope: 0.12 × 87 = $10.44/MMBtu (plus any constant). 10% is 8.7, add 2% (1.74) = 10.44.
- Interpretation: full oil parity would be 100% / 5.8 = 17.2% slope; a 12% slope is ~70% of oil parity, which is the traditional Asian discount.
- Compare with a gas hub: if TTF is $11/MMBtu the oil-linked contract is $0.56 cheaper; if TTF is $9 it is $1.44 dearer.
**Pushback:**
- "What slope makes LNG equal to a $9 TTF at $87 Brent?" (9 / 87 = 10.3%.)
- "Convert $15/MMBtu to EUR/MWh at EURUSD 1.10." (15 × 3.412 = 51.2 $/MWh; / 1.10 = €46.5/MWh.)
**Red flags:** Doesn't know 5.8, or multiplies instead of divides.

### Q4. TTF is €35/MWh and EURUSD is 1.08. What is TTF in $/MMBtu?
**Difficulty:** 1
**Model answer:**
- $/MWh = 35 × 1.08 = $37.80. $/MMBtu = 37.80 / 3.412 ≈ $11.08/MMBtu.
- Shortcut: divide by 3.4 (37.8 / 3.4 = 11.1) — the error from using 3.4 instead of 3.412 is 0.35%, fine for a first pass.
- Quicker still: EUR/MWh × 0.32 ≈ $/MMBtu at EURUSD ~1.08-1.10 (1.08 / 3.412 = 0.3165). 35 × 0.32 = 11.2.
- Reverse: $/MMBtu × 3.412 / EURUSD = EUR/MWh; $10/MMBtu at 1.08 = €31.6/MWh.
- Why it matters: the US-Europe LNG arb and coal-gas switching are both compared in $/MMBtu or $/MWh — you must convert instantly.
**Pushback:**
- "Henry Hub is $3.00. What's TTF minus HH, and does a US cargo with a $2.50 fee make money delivered to Europe?" (11.08 − 3.00 = $8.08. Delivered cost = 1.15 × 3 + 2.50 + ~1.50 shipping + 0.30 regas = $7.75 → ~$3.33/MMBtu margin, yes.)
- "EURUSD drops to 1.00. TTF in $/MMBtu?" (35 / 3.412 = $10.26 — a 7.4% fall with no change in the euro price.)
**Red flags:** Forgets the FX step or divides by 3.412 before converting currency (order doesn't matter mathematically, but forgetting one step does).

### Q5. A 2 million barrel cargo is priced at $78.50. What's it worth? And what's the value of a $0.25 differential on it?
**Difficulty:** 1
**Model answer:**
- 2,000,000 × 78.50 = $157 million. Shortcut: 2 × 78.5 = 157, then add six zeros.
- $0.25/bbl differential on 2m bbl = $500,000. Every $0.01/bbl on a VLCC is $20,000 — useful anchor: a VLCC is "$20k per cent".
- Aframax (700k bbl): $0.01 = $7,000; Suezmax (1m bbl): $0.01 = $10,000. Memorise these to size quality claims and differential negotiations instantly.
- A $1 move in flat price on the unhedged cargo is $2m; that is why it is hedged on day one.
**Pushback:**
- "The buyer asks for a 0.3% quantity tolerance in their favour. What does that cost you?" (0.3% × 2m = 6,000 bbl × 78.5 = $471k.)
- "The cargo prices over five days and the average comes out at $78.90. What's the difference on the cargo?" ($0.40 × 2m = $800k.)
**Red flags:** Gets the order of magnitude wrong (millions vs billions).

### Q6. 500 lots of Brent and the price moves $0.40 against you. What's the P&L? And on 40 lots of LME copper with a $150/t move in your favour?
**Difficulty:** 1
**Model answer:**
- Brent: 500 lots × 1,000 bbl × $0.40 = −$200,000. Shortcut: 500k bbl × 0.40 = 200k.
- Copper: 40 lots × 25 t = 1,000 t × $150 = +$150,000.
- Anchors: 1 Brent lot × $1 = $1,000; 1 copper lot × $1/t = $25; 1 copper lot × $100/t = $2,500; 1 nickel lot (6 t) × $1,000/t = $6,000.
- Variation margin: the Brent loss is cash out the door tomorrow; the copper gain on LME is paid at prompt unless you're on a cleared/margined account — know the difference between realised and unrealised.
- Combined: net −$50,000 on the day, but the two positions are different books and different risks — don't net them in your head when reporting.
**Pushback:**
- "Brent is in $/bbl, what's the same P&L in $/t on the cargo?" ($0.40 × 7.33 = $2.93/t.)
- "How many copper lots equal the same dollar risk as 500 Brent lots if Brent daily vol is $2/bbl and copper is $200/t?" (Brent risk: 500k × 2 = $1m; copper per lot: 25 × 200 = $5,000; 1,000,000 / 5,000 = 200 lots.)
**Red flags:** Uses 100 bbl per lot, or forgets the 25 t copper lot.

### Q7. Financing cost of a $190 million cargo for 30 days at 6% per annum? Per barrel on 2 million barrels?
**Difficulty:** 1
**Model answer:**
- 190m × 0.06 × 30 / 360 = 190m × 0.005 = $950,000. Shortcut: 6% a year is 0.5% a month; 0.5% of 190m is 950k.
- Per barrel: 950,000 / 2,000,000 = $0.475/bbl. Or: cargo price is $95/bbl; 0.5% of 95 = $0.475.
- Rule of thumb: financing in $/bbl/month = price × annual rate / 12. At $80 and 6%: $0.40. At $80 and 3%: $0.20.
- Why it matters: it's the second-largest component of carry after storage and it scales with price; high rates and high prices make contango less attractive to store into.
- Day-count convention: money markets use 360; if the trader uses 365 the answer is $937k — say which you used.
**Pushback:**
- "Same cargo, 45 days, 7.5%." (190m × 0.075 × 45/360 = 190m × 0.009375 = $1.78m.)
- "Your LC is confirmed at 1.5% p.a. on top. What's the all-in?" (7.5% + 1.5% = 9%; 190m × 0.09 × 45/360 = $2.14m.)
**Red flags:** Uses a full year of interest, or can't do 0.5% of 190m.

### Q8. Vessel time charter is $45,000/day, round-trip voyage is 60 days including port time, cargo 2 million barrels. Freight per barrel? Then add bunkers.
**Difficulty:** 2
**Model answer:**
- Hire: 45,000 × 60 = $2.7m; / 2m bbl = $1.35/bbl.
- Time charter hire excludes fuel and port costs (the charterer pays those), so add bunkers: ~50 t/day × 45 sailing days × $550/t ≈ $1.24m → $0.62/bbl. Port costs and canal fees say $200k → $0.10/bbl.
- All-in ≈ $1.35 + 0.62 + 0.10 ≈ $2.07/bbl, i.e. about $15/t for Brent-type crude.
- Shortcuts: $/bbl = ($/day × days) / bbl; for a VLCC every $10,000/day on a 60-day voyage is $0.30/bbl. Bunkers: 50 t/day is a typical laden/ballast average for a VLCC at eco speed; every $100/t on bunkers is ~$0.11/bbl on this voyage.
- Compare with the spot market: if spot Worldscale on the route gives $2.50/bbl, your time-chartered ship is $0.43/bbl in the money — a $860k advantage on the cargo.
**Pushback:**
- "The vessel waits 5 extra days at the discharge port. What does that do to $/bbl?" (5 × 45,000 = $225k, plus fuel at anchor; ≈ $0.11-0.12/bbl; if the delay is the receiver's fault, you claim demurrage.)
- "Ballast leg is 45% of the round trip. What's the effective laden cost per day?" (You still pay for the ballast days; that's why the round trip is used — but a backhaul cargo could cut the effective cost.)
**Red flags:** Divides hire by one-way days only, or forgets bunkers on a time charter.

### Q9. The Worldscale flat rate for a route is $18.00/t and the fixture is WS 65. What is the freight in $/t and $/bbl for Brent-type crude?
**Difficulty:** 2
**Model answer:**
- $/t = flat rate × WS / 100 = 18 × 0.65 = $11.70/t.
- $/bbl = 11.70 / 7.33 ≈ $1.60/bbl (11.7 / 7 = 1.67; adjust down ~4.5% for the .33 → 1.60).
- Shortcut: at flat rate $18, every WS point is $0.18/t or ~$0.0246/bbl; so WS 65 ≈ 65 × 0.0246 = $1.60. Every 10 WS points ≈ $0.25/bbl on this route.
- On a 2m bbl cargo: $1.60 × 2m = $3.2m freight.
- Remember: the flat rate is reset annually (bunkers, port costs), so WS 65 this year is not the same $/t as WS 65 last year; compare $/t or TCE across years, not WS.
**Pushback:**
- "Rates jump to WS 110 on a sanctions headline. New freight per barrel and total?" (18 × 1.10 = $19.80/t; / 7.33 = $2.70/bbl; × 2m = $5.4m; the increase of $1.10/bbl is $2.2m on the cargo.)
- "Same WS on a Suezmax route with flat rate $25. Per barrel?" (25 × 0.65 = $16.25/t; / 7.33 = $2.22/bbl — smaller ships cost more per barrel.)
**Red flags:** Treats WS 65 as $65/t or as $/bbl.

### Q10. RBOB is $2.45/gal, ULSD is $2.60/gal, WTI is $75/bbl. What's the 3-2-1 crack?
**Difficulty:** 2
**Model answer:**
- Convert products to $/bbl: RBOB 2.45 × 42 = $102.90; ULSD 2.60 × 42 = $109.20.
- Crack = (2 × 102.90 + 1 × 109.20 − 3 × 75) / 3 = (205.80 + 109.20 − 225.00) / 3 = 90.00 / 3 = $30.00/bbl.
- Shortcut for × 42: multiply by 40 and add 5% (2.45 × 40 = 98; + 4.9 = 102.9). For the crack: work in the product-minus-crude gaps: gasoline crack = 102.9 − 75 = 27.9; diesel crack = 109.2 − 75 = 34.2; 3-2-1 = (2 × 27.9 + 34.2) / 3 = 90 / 3 = 30.
- Interpretation: distillate crack (34.2) is above gasoline (27.9) — a distillate-led margin; a refiner maximises diesel yield.
- Per $0.01/gal move in RBOB the 3-2-1 moves 2/3 × 0.42 = $0.28/bbl; per $0.01/gal in ULSD, 1/3 × 0.42 = $0.14/bbl.
**Pushback:**
- "RBOB drops 10 c/gal. New crack?" (RBOB 2.35 × 42 = 98.70; crack = (197.4 + 109.2 − 225) / 3 = 81.6 / 3 = $27.20 — down $2.80, consistent with the $0.28 per cent rule.)
- "What's the crack in $/gal terms?" (30 / 42 = $0.714/gal.)
**Red flags:** Forgets the × 42, or divides by 3 in the wrong place.

### Q11. Brent M1-M2 contango is $1.00/bbl. Storage is $0.45/bbl/month, financing is 0.5% per month on an $80 barrel, insurance $0.02. Does it pay to store 1 million barrels for a month?
**Difficulty:** 2
**Model answer:**
- Carry = storage 0.45 + financing (0.5% × 80 = 0.40) + insurance 0.02 = $0.87/bbl/month.
- Contango 1.00 − carry 0.87 = $0.13/bbl margin; × 1m bbl = $130,000 per month. Yes, it pays, but thinly.
- Mechanics: buy prompt, sell M2 futures (1,000 lots), put oil in tank, deliver against or roll out of the short at the deferred price. The margin is locked once both legs are done.
- Sensitivity: if storage is $0.55 or financing rises to 0.65%/month (7.8% p.a.), the trade is at or below breakeven; if the contango was $0.90 you'd lose $0.02 × 1m = $20k. The trade is a bet on the cost side being fixed — lock the tank rate.
- What else eats the $0.13: pumping/throughput fees, in-tank losses (~0.1%, i.e. $0.08/bbl at $80), quality degradation, and the risk the contango narrows before you've put the hedge on.
**Pushback:**
- "Now it's a 12-month contango of $6. Annual carry?" (0.87 × 12 = $10.44 → doesn't pay; contango would need to be above ~$10.50 for a 12-month store at these costs, and long-dated storage is usually cheaper per month, so recompute with the actual rate.)
- "You've got floating storage at $30,000/day on a VLCC. What's that per barrel per month?" (30,000 × 30 = $900k / 2m = $0.45/bbl/month — the same as the tank in this example, plus bunkers at anchor.)
**Red flags:** Compares the contango to storage cost alone and forgets financing.

### Q12. You blend 600,000 bbl bought at $82.00 with 400,000 bbl bought at $79.50. What's the weighted average cost of the 1 million barrel cargo?
**Difficulty:** 1
**Model answer:**
- (600,000 × 82.00 + 400,000 × 79.50) / 1,000,000 = (49,200,000 + 31,800,000) / 1,000,000 = $81.00/bbl.
- Shortcut: start at the higher price and move toward the lower one by the smaller weight × the gap: 82 − 0.4 × 2.50 = 82 − 1.00 = 81.00. Or start at 79.50 + 0.6 × 2.50 = 81.00.
- Total cost: $81m. If the blend sells at $81.80, the blending margin is $0.80 × 1m = $800k before costs.
- Extend to quality: if the blend needs to hit a sulphur spec, the same weighted-average logic applies to the sulphur content (mass-weighted, not volume-weighted, strictly, but volume is a fine first pass for similar densities).
- On a desk, you also weight the pricing periods: if the two parcels priced on different days, the blended cargo's hedge has to be split the same way.
**Pushback:**
- "Add 200,000 bbl at $84. New average?" ((81 × 1m + 84 × 0.2m) / 1.2m = (81 + 16.8) / 1.2 = 97.8 / 1.2 = $81.50.)
- "What's the max you can pay for the 400k parcel and still average $81?" (If 600k at 82 and average 81 on 1m: 81m − 49.2m = 31.8m / 400k = $79.50 — the same as before; i.e. every $1 on the small parcel moves the average by $0.40.)
**Red flags:** Takes the simple average of the two prices ($80.75).

### Q13. Chicago wheat is at 650 c/bu and corn at 450 c/bu. Convert both to $/t.
**Difficulty:** 2
**Model answer:**
- Wheat: 650 c/bu = $6.50/bu × 36.74 bu/t = $238.8/t.
- Shortcut: × 36.74 ≈ × 37 minus 0.7%: 6.5 × 37 = 240.5; minus 0.26 × 6.5 (= 1.7) = 238.8.
- Corn: 450 c/bu = $4.50/bu × 39.37 bu/t = $177.2/t. Shortcut: × 40 minus 1.6%: 4.5 × 40 = 180; minus 0.63 × 4.5 (= 2.8) = 177.2.
- Anchors: for wheat/soybeans, $1/bu ≈ $36.74/t; for corn, $1/bu ≈ $39.37/t. A 10 c/bu move = $3.67/t (wheat) or $3.94/t (corn).
- Why different: a bushel is a volume; corn is denser (56 lb/bu) than wheat and soybeans (60 lb/bu), which is why the conversions differ (1 t = 2,204.6 lb; / 60 = 36.74; / 56 = 39.37).
**Pushback:**
- "Paris milling wheat is €230/t at EURUSD 1.08. Which is cheaper, Chicago or Paris, on a $/t basis?" (Paris = $248.4/t vs Chicago $238.8/t → Chicago cheaper by ~$9.6/t before quality and freight.)
- "A 5,000 bu CBOT wheat lot moves 15 c. P&L?" (5,000 × 0.15 = $750 per lot.)
**Red flags:** Doesn't know a bushel is a volume with a different weight per grain.

### Q14. Quick fire: 17 × 23; 1/7 as a decimal; 4.5% of 220 million; 0.6% of 1.98 million barrels.
**Difficulty:** 1
**Model answer:**
- 17 × 23 = 391. Shortcut: (20 − 3)(20 + 3) = 400 − 9 = 391.
- 1/7 = 0.142857 (repeating). Memorise the sevenths: 0.142857, 0.285714, 0.428571, 0.571428, 0.714285, 0.857142 — the same six digits cycled. Useful because 7.33 bbl/t ≈ 22/3 and dividing by 7 crops up constantly.
- 4.5% of 220m: 1% = 2.2m; × 4.5 = 9.9m. Or 10% = 22m, halve to 5% = 11m, less 0.5% (1.1m) = 9.9m.
- 0.6% of 1.98m bbl: 1% = 19,800; × 0.6 = 11,880 bbl (≈ 12,000 bbl, i.e. about $950k at $80 — a typical quantity-tolerance or loss figure on a VLCC).
- Other staples: 1/6 = 0.1667; 1/8 = 0.125; 1/12 = 0.0833; 1/42 = 0.0238; √252 ≈ 15.9; 1.06^5 ≈ 1.34.
**Pushback:**
- "23 × 47?" (23 × 50 − 23 × 3 = 1,150 − 69 = 1,081.)
- "What's 6% compounded monthly over a year, roughly?" ((1 + 0.005)^12 ≈ 1.0617, i.e. 6.17%.)
**Red flags:** Reaches for a phone, or freezes on 1/7.

### Q15. Copper falls from $9,850/t to $9,260/t. What's the percentage? And what is that on a book that's long 320 lots?
**Difficulty:** 1
**Model answer:**
- Move: 9,850 − 9,260 = $590. 590 / 9,850 ≈ 6.0%. Shortcut: 6% of 9,850 = 591 — so it's essentially exactly −6%.
- 320 lots × 25 t = 8,000 t; × $590 = −$4.72m.
- Shortcut for tonnage: LME lots × 25 — 320 lots is 8,000 t (32 × 250). Per $100/t on 8,000 t = $800k; × 5.9 = $4.72m.
- If the book is a hedged physical long (short futures against physical inventory) the flat-price loss on physical is offset by the futures gain; the residual is the premium/differential, so the number to worry about is the physical premium move, not the $4.72m.
- Annualised context: if copper's daily vol is ~1.5%, a 6% day is a four-sigma event — check for a squeeze unwind, a tariff headline or a China data shock.
**Pushback:**
- "How much does copper have to rally from $9,260 to get back to $9,850 in percent?" (590 / 9,260 = 6.37% — more than the 6% fall.)
- "In $/lb?" (9,260 / 2,204.6 = $4.20/lb; the $590 move is 26.8 c/lb.)
**Red flags:** Says −5.9% or −6.4% without knowing which base was used.

### Q16. Demurrage: $35,000/day, laytime allowed 36 hours, the vessel was on demurrage for 4.5 days from NOR. What is the claim, and what is it per barrel on a 700,000 bbl Aframax?
**Difficulty:** 2
**Model answer:**
- Time on demurrage = total time from NOR to completion minus allowed laytime: 4.5 days − 1.5 days = 3.0 days.
- Claim = 3.0 × $35,000 = $105,000. Demurrage is pro rata, so 3 days 6 hours would be 3.25 × 35,000 = $113,750.
- Per barrel: 105,000 / 700,000 = $0.15/bbl. Rule: every day of demurrage on an Aframax at $35k/day is $0.05/bbl; on a VLCC at $50k/day it's $0.025/bbl.
- Contract point: check who pays — the buyer under a CIF sale, the seller under FOB if the delay was at load port — and whether the contract caps demurrage or requires notice within a fixed period (claims are often time-barred after 60-90 days).
- Also check the NOR was valid (tendered at the right place and time, free pratique), and whether any time is excluded (weather, shifting, the first 6 hours after NOR under some charter parties).
**Pushback:**
- "Half of the delay was because your supplier's documents were late. Who eats it?" (You, unless your purchase contract passes it through; this is why back-to-back demurrage terms matter.)
- "The demurrage rate was WS-linked in the charter party. What does that mean?" (Demurrage rises with the market; if the fixture was at WS 100 and the market is WS 180, the demurrage rate may be reset to the market — read the clause.)
**Red flags:** Charges demurrage for the full 4.5 days.

### Q17. Diesel is $720/t FOB ARA. MR freight to Lagos is $45/t, financing 25 days at 6%, in-transit losses 0.3%, insurance $1/t, port and inspection $3/t. What is the landed cost in $/t and $/bbl, and what CIF West Africa price makes the arb work?
**Difficulty:** 3
**Model answer:**
- Financing: 720 × 0.06 × 25 / 360 = 720 × 0.004167 = $3.00/t.
- Losses: 0.3% × 720 = $2.16/t.
- Landed = 720 + 45 + 3 + 2.16 + 1 + 3 = $774.16/t ≈ $774/t.
- $/bbl at 7.45 bbl/t for diesel: 774 / 7.45 ≈ $103.9/bbl. (7.45 × 100 = 745; remainder 29 / 7.45 ≈ 3.9.)
- Breakeven: CIF West Africa must exceed $774/t; a trader wants a margin of, say, $8-10/t to cover demurrage risk and hedging slippage, so the arb "works" at roughly $783+/t. On a 37,000 t MR that $9/t is ~$333k gross.
- Hedge: sell the destination index (or fix the sale price) and buy the origin index as swaps for the pricing periods; you're left with the spread plus freight and basis. If freight isn't fixed, you're also long freight.
**Pushback:**
- "Freight rises to $60/t and financing to 8%. New breakeven?" (Financing 720 × 0.08 × 25/360 = $4.00; landed = 720 + 60 + 4 + 2.16 + 1 + 3 = $790.16/t.)
- "The buyer wants 30 days' credit. What does that add?" (Another 30 days at 6% on ~$774: 774 × 0.06 × 30/360 = $3.87/t — either add it to price or price it into the credit terms.)
**Red flags:** Forgets a component, or converts $/t to $/bbl with 7.33 (crude) instead of ~7.45 (diesel).

### Q18. Henry Hub is $3.00, the liquefaction fee is $2.50, shipping to Europe $1.50, regas $0.30, TTF is $11/MMBtu. What's the margin per MMBtu and per cargo?
**Difficulty:** 2
**Model answer:**
- FOB cost = 1.15 × 3.00 + 2.50 = 3.45 + 2.50 = $5.95/MMBtu.
- Delivered = 5.95 + 1.50 + 0.30 = $7.75. Margin vs TTF = 11.00 − 7.75 = $3.25/MMBtu.
- Cargo: ~3.5 TBtu = 3,500,000 MMBtu; × 3.25 = $11.4m per cargo (3.5 × 3.25 = 11.375).
- Shortcut: at HH $3, 15% is $0.45 — call the variable gas cost "HH + 15%"; and know the fee is sunk: the variable-cost floor for lifting is 3.45 + 1.50 + 0.30 = $5.25, so TTF would have to fall below $5.25 before cancelling makes sense.
- Add boil-off (~0.1%/day × 15 days = 1.5% of the cargo) and the margin falls by ~$0.12/MMBtu at these prices — a strong candidate mentions it.
**Pushback:**
- "JKM is $12.50 and shipping to Asia is $3.00. Europe or Asia?" (Asia nets 12.50 − 3.00 − 0.30 = 9.20 vs Europe 11.00 − 1.50 − 0.30 = 9.20: indifferent at these numbers — so it comes down to canal availability, ship days and the next cargo's positioning.)
- "HH rises to $4.50. New margin to Europe?" (1.15 × 4.5 = 5.175 + 2.5 + 1.5 + 0.3 = 9.475; margin = $1.525/MMBtu → $5.3m per cargo.)
**Red flags:** Forgets the 115%, or treats the fee as a variable cost when deciding to cancel.

### Q19. You hold 2 million barrels in a market that is $0.60/bbl backwardated month-on-month. What does it cost to hold them for three months, and what spread would you need to store instead?
**Difficulty:** 2
**Model answer:**
- Holding into backwardation loses the spread every month on the hedge roll (you are long physical, short futures; each month you buy back the expiring short at a higher price and sell the next month lower): 2,000,000 × 0.60 = $1.2m per month; × 3 = $3.6m.
- Plus physical carry (storage, financing, insurance) of ~$0.85/bbl/month: another 2m × 0.85 × 3 = $5.1m. Total cost of holding ≈ $8.7m over three months, or $4.35/bbl.
- To store profitably you'd need a contango greater than carry: > $0.85/bbl/month, i.e. a swing of ~$1.45/bbl/month from the current spread.
- Rule of thumb: in backwardation, sell prompt and buy back later; do not hold inventory beyond operational minimum. In contango wider than carry, fill every tank you have.
- On a desk this shows up as negative "roll yield" in the P&L explain — a hedged inventory book bleeds in backwardation even if flat price is unchanged.
**Pushback:**
- "The backwardation is $0.60 for M1-M2 but only $0.30 for M2-M3 and $0.20 for M3-M4. Recompute." (2m × (0.60 + 0.30 + 0.20) = 2m × 1.10 = $2.2m in roll cost, not $3.6m — always use the actual curve, not a constant.)
- "Why would anyone hold inventory in backwardation?" (Operational minimums, contractual delivery obligations, quality blending stock, or a view that the front spread will spike further — a speculative long on tightness.)
**Red flags:** Says backwardation makes inventory profitable, or ignores physical carry.

### Q20. You have 12,000 dry tonnes of copper concentrate at 28% Cu, payable 96.5%. How many tonnes of copper do you hedge, and how many LME lots? If TC is $80/t and RC 8 c/lb, what do you pay the smelter?
**Difficulty:** 3
**Model answer:**
- Contained copper: 12,000 × 0.28 = 3,360 t. Payable: 3,360 × 0.965 = 3,242 t.
- Lots: 3,242 / 25 = 129.7 → hedge 130 lots (or 129 and accept a 17 t under-hedge).
- Payable value at $9,000/t: 3,242 × 9,000 ≈ $29.2m.
- TC: $80/dmt × 12,000 = $960,000. RC: 8 c/lb × 3,242 t × 2,204.6 lb/t = 0.08 × 7,147,000 lb ≈ $571,800. Total charges ≈ $1.53m, i.e. ~$127/t of payable copper, or ~5.2% of the payable value at $9,000.
- Shortcut for RC: 1 c/lb ≈ $22.05/t, so 8 c/lb ≈ $176/t of payable copper; × 3,242 t ≈ $571k.
- Timing: the quotational period is usually a month or more after arrival, so the 130 lots go in the month the concentrate prices, not the shipping month; and the hedge is adjusted when the final assay replaces the provisional one.
**Pushback:**
- "Final assay comes in at 27.4% Cu. What changes?" (Contained 3,288 t; payable 3,173 t; ~127 lots — you're over-hedged by 3 lots (69 t), buy them back; the provisional invoice is trued up.)
- "TC/RCs fall to $20/t and 2 c/lb. How much does the miner gain on this shipment?" (TC: 12,000 × 60 = $720k; RC: 6 c/lb × 7.147m lb = $429k; total ≈ $1.15m more revenue to the miner — that's why low TC/RCs matter.)
**Red flags:** Hedges the gross contained tonnes, or forgets the pound conversion on the RC.

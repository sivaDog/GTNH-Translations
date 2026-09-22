# ja_JP forceload/betterquesting 未翻訳ブロック一覧

対象ファイル: `ja_JP/config/txloader/forceload/betterquesting/lang/ja_JP.lang`
生成日: 2026-09-22

## 検出方法

- `.name=` / `.desc=` の値にひらがな・カタカナ・漢字が1文字も含まれない行を「未翻訳」と判定。
- クエスト単位(コメント行+name+desc)でグルーピングし、name/descのどちらかでも未翻訳なら
  そのクエスト全体をブロックに含める。
- 空行を挟んでも直後のクエストが未翻訳なら同じブロックとして連結。翻訳済みクエストが
  1つでも間に挟まればブロックを区切る。
- 値が `[下書き]` で始まる場合は日本語を含んでいても未翻訳扱い(下書きは正式訳ではないため)。
- `# Quest:` 等のコメント行自体は判定対象外。表示では `Quest:` / `Quest Line:` 接頭辞を省略。
- `## Quest Line:` 単位を「章」として、各ブロックが属する章でグループ化。
- 翻訳確認は2.8.4のゲームインスタンスで行うが、翻訳作業はv2.9(master)側。
  個々のクエストのIDを2.8.4実機のクエストDBとv2.9(GT-New-Horizons-Modpack)の
  クエストDBで突き合わせ、次の3パターンを判定(questlineは対象外):
  - 2.8.4のみに存在(v2.9で削除): この資料から除外し、翻訳作業もしない。
  - v2.9のみに存在(2.8.4に無い新規クエスト): 資料には残すが「⚠v2.9新規」を付け、
    ゲーム内で確認できないため翻訳作業はしない。
  - 同じIDだが中身(name)が別クエストに変わっている(ID使い回し): 同様に「⚠ID使い回し」を付け、
    ゲーム内表示は旧クエストのままなので翻訳作業はしない。

## 除外した誤検出(15件)

nameのみが未翻訳判定でdescは翻訳済み、かつnameが化学式・元素記号・Tier表記(`Tier N (XX)`)・
Mod名・本文中でも英語のまま使われる固有名詞など、翻訳不要と判断できるもの。

- L1004 C9H8O4...NaCl...H2O...
- L1112 LPG
- L1749 Tier 2 (MV)
- L1761 HCL
- L2042 Tier 3 (HV)
- L2442 NaK
- L2463 Tier 4 (EV)
- L4096 Tier 9 (UHV)
- L5223 Weed-EX
- L6494 Botany
- L6630 Carpenter's Blocks
- L10257 Applied Energistics
- L12172 Hardcore End(er) Expansion
- L14855 Better Questing?
- L15422 Trigger: Loot Game

## バージョン差異による除外(3件)

2.8.4のクエストDBにのみ存在し、v2.9(master)では削除されているクエスト。
この資料には載せず、翻訳作業の対象にもしない。

- L15609 [下書き]遺伝学者の道具
- L15612 [下書き]分析機
- L15615 [下書き]接続機

## サマリー

- ファイル内の全クエスト/クエストライン数: 3859(誤検出・バージョン差異除外後 3841)
- 未翻訳率: 2128/3841 (55%)
  - うち `[下書き]` 表記(未訳扱い): 63件
  - うち ⚠バージョン差異で翻訳作業を保留: 137件
- 連続ブロック数: 246

## 進捗(前回資料生成からの差分)

基準: 前回資料生成時点(2026-09-19) との比較。

- この基準以降に翻訳が完了したクエスト: 5件
- この基準以降に新規追加された未翻訳クエスト(フォーク元の更新等): 0件

翻訳完了したクエスト一覧:

- L9305 Oxygen Tanks
- L10212 EVEN EVEN BETTER CHASSIS
- L11921 Solum
- L11925 Ignis
- L12157 Volcanic

## 章ごとの未翻訳ブロック

### ヒントとコツ  _(L137)_ — 未翻訳率: 1/6 (17%)

- [ ] L157-L159 (1) Build Your Own Keep Inventory

### Tier 1 - LV時代  _(L856)_ — 未翻訳率: 3/143 (2%)

- [ ] L1408-L1410 (1) Steam Regulator
- [ ] L1420-L1426 (2) Reading the Grid / Void Buses⚠

### Tier 2 - MV時代  _(L1437)_ — 未翻訳率: 8/141 (6%)

- [ ] L1925-L1927 (1) Grinding Heads Are Better Than None
- [ ] L1945-L1947 (1) Make a better Distillery
- [ ] L1985-L2007 (6) MV Wiremill⚠ / MV Cutting Machine⚠ / Dislocator Inhibitor⚠ / String Theory?⚠ / Still No Filing in MV⚠ / Conduit Probe

### Tier 3 - HV時代  _(L2010)_ — 未翻訳率: 6/107 (6%)

- [ ] L2022-L2024 (1) Personal Dimension⚠
- [ ] L2350-L2356 (2) UUMatter / MV Field Generator
- [ ] L2426-L2436 (3) Fluoro-who now?⚠ / Melting and Refreezing⚠ / Ender Fluid Conduits

### Tier 4 - EV時代  _(L2447)_ — 未翻訳率: 51/85 (60%)

- [ ] L2567-L2605 (10) Nano Supercomputer / EV Chemical Bath / Nano Mainframe / Blue Steel / EV Circuit Assembler / Epoxid … 他4件
- [ ] L2611-L2637 (7) EV Laser Engraver / EV Superconductors (2048 EU/t) / Pure Uranium Ores / Want to Join a Band? / Radon Decay / Sodium Sulfide … 他1件
- [ ] L2643-L2673 (8) Ender Egg / Draconium Egg / Dragon Egg Omlet / Glass Fiber / Fiber Reinforced Epoxid Sheet / Empty Fiber Reinforced Glass Board … 他2件
- [ ] L2679-L2721 (11) Data Orbs / Create New Materials Out of Pure Energy / Critical Materials / What's in the Box? / Platinum Processing, Step 4 / Platinum Processing, Step 3 … 他5件
- [ ] L2727-L2765 (10) Just Enough Tungstensteel For Your Rocket / Bigger Drums / Dichlorobenzene / Polyphenylene Sulfide / Higher Tier Cables / Advanced Ilmenite Processing … 他4件
- [ ] L2771-L2789 (5) Niobium-Titanium / Four fluids in the one Hatch! / EV Field Generator / HV Field Generator / EXTREME MIXING

### Tier 5 - IV時代  _(L2792)_ — 未翻訳率: 127/131 (97%)

- [ ] L2796-L2822 (7) IV Field Generator / Tier 5 (IV) / On Your Way to Asteroids and Other Rocket Tier 3 DIMs / Callisto Trip / Europa Trip / IV Superconductors (8192 EU/t) … 他1件
- [ ] L2828-L2938 (28) You're Gonna Hate This 5 and 6 in IV / Ceres Trip / Quantum Star / HSS-S / Argon / Your First Naquadah Ingot … 他22件
- [ ] L2944-L2966 (6) Quantum Supercomputer / Quantum Mainframe / Cheaper LV Circuits / On Your Way to Tier 4 DIMs / Mercury Trip / Venus Trip
- [ ] L2972-L3314 (86) IV Assembler / Palladium Processing / Platinum Group Processing - All the Other Metals / First Separation - Rhodium / Second Separation - Ruthenium / Re-Solving the Purity Issue … 他80件

### Tier 6 - LuV時代  _(L3317)_ — 未翻訳率: 76/78 (97%)

- [ ] L3321-L3355 (9) Netherite Scrap Seed / Dense Netherite Plate / Nefarious Production / Hot Netherite Scrap / Netherite Materials / Automated Mining … 他3件
- [ ] L3361-L3627 (67) Now You're Really Gonna Hate This 5 and 6 in LuV / Tier 6 (LuV) / Fluid TP for Magic-Haters / Thought Emitters Were Bad Enough? / Accelerating Things II / Accelerating Things III … 他61件

### Tier 7 - ZPM時代  _(L3630)_ — 未翻訳率: 49/65 (75%)

- [ ] L3634-L3640 (2) Prismatic Naquadah Composite Slurry / Prismatic Acid
- [ ] L3686-L3708 (6) Energy Infuser / Fusion Reactor MKII - Bigger, Better, Fusor / Making Americium / Learning Curve? Where We're Going There Are No Curves / The Beginning of the End Game / Tier 7 (ZPM)
- [ ] L3714-L3788 (19) You Can't Get Enough of This Pt 2 in ZPM / ZPM Superconductors (131,072 EU/t) / ZPM Field Generator / ZPM Assembler / ZPM Energy Hatch / Europium Doped Wafers … 他13件
- [ ] L3794-L3828 (9) Concentration / Recycle Trinium / Linear Accelerator / Refining / N.N.Q.Q.N.Q.Q / Purification … 他3件
- [ ] L3838-L3888 (13) Prismarine Recycling Pt. 2 / Prismarine Solution / Prismarine!? What Do I Need That For? / Prismatic Gas / Wormhole Generator⚠ / Naquarite Universal Insulator Foil … 他7件

### Tier 8 - UV時代  _(L3891)_ — 未翻訳率: 41/43 (95%)

- [ ] L3899-L4061 (41) I Put Fusion in Your Fusion so you Can Fusion While You Fusion / Time for Another Reactor / Americium Doped Wafers / Quantum Computer / Research Station / Maintenance Free At Last! … 他35件

### Tier 9 - UHV時代  _(L4064)_ — 未翻訳率: 30/34 (88%)

- [ ] L4068-L4078 (3) Draconic Core / Quantum Anomaly / Wyvern Core
- [ ] L4084-L4094 (3) Infinite Vis Storage, kinda? / Infinite Oxygen Tank / Misc Endgame Goals
- [ ] L4108-L4202 (24) UHV Superconductors (2,097,152 EU/t) / UHV Field Generator / UHV Energy Hatch / Assembling Living Circuits / The Final Frontier? / It's Not Going Bad, I Swear! … 他18件

### Tier 10 - UEV時代  _(L4205)_ — 未翻訳率: 53/55 (96%)

- [ ] L4209-L4267 (15) Capturing Light on a Circuit Board / Stopping the Infinity Bleed / My Eyes Hurt! #2 / NAC™: Advanced Routing Package⚠ / NAC™: Fundamentals Package / Awakened Core … 他9件
- [ ] L4273-L4423 (38) Longbow of the Heavens / My Eyes Hurt! #4 / Tesseract / Dragonblood / Metastable Oganesson / Infinity Boots … 他32件

### Tier 11 - UIV時代  _(L4426)_ — 未翻訳率: 45/46 (98%)

- [ ] L4430-L4609 (45) Bending Space and Time / Quantum Tank X / Heliofusion Exoticizer / A Fork in The Road / Tunnels Of Light / Dyson Swarm Modules⚠ … 他39件

### Tier 12 - UMV時代  _(L4612)_ — 未翻訳率: 44/45 (98%)

- [ ] L4616-L4790 (44) T4: Advanced / Finally, Universium! / Wireless Multi-Amp Hatches / Magnetohydrodynamically Constrained Star Matter / Guzzling Massive Amounts of Gas / UMV Energy Hatch … 他38件

### エンドゲーム - ゴール  _(L4793)_ — 未翻訳率: 29/30 (97%)

- [ ] L4797-L4911 (29) A Universe In Your Drives⚠ / MAX Circuits / Strings Upon Strings Upon Strings Upon-⚠ / Tier 13 (UXV) / The Door to Heaven? / Stargate Ring Block … 他23件

### 自給自足  _(L4914)_ — 未翻訳率: 8/48 (17%)

- [ ] L5026-L5028 (1) Dezil's Marshmallow
- [ ] L5050-L5064 (4) Really OP Food / Uncooked Slush / Glowing Marshmallow / Cooling Your Marshmallow
- [ ] L5098-L5113 (3) A Magical Lunchbox? / Ice Ice Baby⚠ / The Green Revolution

### 緑の革命  _(L5111)_ — 未翻訳率: 1/162 (1%)

- [ ] L5367-L5369 (1) Platina

### 旅に出かけよう...  _(L5764)_ — 未翻訳率: 24/65 (37%)

- [ ] L5768-L5770 (1) Indestructible Vessel
- [ ] L5776-L5778 (1) Relocator
- [ ] L5812-L5814 (1) Advanced Electric Jetpack
- [ ] L5908-L5910 (1) Travelocity!
- [ ] L5916-L5926 (3) Angel Wings / Secret-Angel-Assasin / Angel Wings - Ultra Force!
- [ ] L5944-L5978 (9) Better Boots with a little pizzazz / Walk all over you / Walking across the stars / Flying Like....Mary Poppins? / Flying With the Greatest of Ease / Working While Flying? … 他3件
- [ ] L5984-L6010 (7) Travelocity² / Let's Go Lava Surfing! / Enhanced Charm of Dislocation / Charm of Dislocation / Planar Gateways / Chaos Locator … 他1件
- [ ] L6020-L6022 (1) Spare Battery

### ...死ぬことなしに  _(L6025)_ — 未翻訳率: 28/99 (28%)

- [ ] L6033-L6043 (3) Protect Your Base: Tier 4 / Make Love, Not War / Why Grenades...
- [ ] L6053-L6067 (4) Protect Your Base: Tier 5 / Turret Base Tier 5 / PewPew! / Railguns, What Else
- [ ] L6093-L6095 (1) Luke, I'm Your Father
- [ ] L6101-L6115 (4) Protect Your Base: Tier 2 / Tier 2 Turret Base / Sometimes, a Bullet Will Do / Burn Them. Burn Them All!
- [ ] L6121-L6139 (5) Protect Your Base: Tier 3 / Tier 3 Base / This is Relatively Useful / Fire in the Hole / Turret Base Tier 4
- [ ] L6205-L6211 (2) Dark Steel Armor Basic Upgrades / Dark Steel Armor Advanced Upgrades
- [ ] L6269-L6291 (6) Nano Goggles / Quantum Goggles / Goggles > 9000 / Compressed Steel Armor / Compressed Desh Armor / Compressed Titanium Armor⚠
- [ ] L6381-L6383 (1) Eldritch Striders⚠
- [ ] L6389-L6391 (1) Apprentice Striders⚠
- [ ] L6401-L6403 (1) Archmage Striders

### キッチリ基地を建築  _(L6422)_ — 未翻訳率: 30/80 (38%)

- [ ] L6426-L6432 (2) Let it Glow! / Barrel Upgrades⚠
- [ ] L6590-L6596 (2) Lighting Up a Large Area, Without Electricity / Lighting Up a Large Area, With Electricity
- [ ] L6602-L6604 (1) BetterIO?
- [ ] L6638-L6664 (7) Excavation Upgrade / Crystal Shulker Box / Let's get Building! / Chests Had Quite the Glow-up!⚠ / Obsidian Barrel / Obsidian Shulker Box … 他1件
- [ ] L6670-L6672 (1) Iron Shulker Box
- [ ] L6678-L6716 (10) Gotta Go Fast! / Gold Shulker Box / Finally, Some Real Power! / Shulker Upgrades / Diamond Shulker Box / Advanced Concrete Backfiller … 他4件
- [ ] L6722-L6748 (7) Advanced Filing Cabinet / Marking Your Base⚠ / Silver Shulker Box / Draconic Chest / Concrete Backfiller / Chiseling the Way Greg Intended … 他1件

### Forestryとマルチファーム  _(L6751)_ — 未翻訳率: 22/68 (32%)

- [ ] L6755-L6759 (1) THE RAINMAKER
- [ ] L6777-L6793 (3) The Multifarm / Farm Logic / Changing Your Foresty Circuit Configuration
- [ ] L6803-L6843 (7) Multifarm: Hatch / Multifarm: Valve / Multifarm: Control / Multifarm: Gearbox / Enhanced Farm Logic / Refined Farm Logic … 他1件
- [ ] L6861-L6883 (4) Copper, Tin, Bronze Tubes / Iron, Golden, Diamantine Tubes / Rubberised, Obsidian, Lapis Tubes / Blazing, Ender, Emerald Tubes
- [ ] L6897-L6919 (4) Another Path to Ethanol / Why No, This is Not Fit For Human Consumption / Better Fermenter Outputs / Such Pretty Leaves...
- [ ] L6925-L6929 (1) Seeing the Fruits of Your Labor
- [ ] L6943-L6945 (1) Speak For the Trees
- [ ] L6995-L6999 (1) U-238 Tu-Wait, Seriously?

### マルチブロックの旅  _(L7066)_ — 未翻訳率: 64/117 (55%)

- [ ] L7070-L7076 (2) Distill the Atmosphere / Collision Course
- [ ] L7138-L7148 (3) An Industrial Mobfarm / Powderbarrels / TNT
- [ ] L7190-L7192 (1) Let's Get Crackin!
- [ ] L7214-L7232 (5) Still Not Enough Charcoal? / It's Time to Get More Steam / Steam is Never Enough / Moooooore Steam / Even More Steam? Are You Sure?
- [ ] L7238-L7244 (2) A Very Useful Scanner / The 'Water Problems' Are Solved
- [ ] L7250-L7268 (5) Assembly Line / Data Access Hatches / Time to Drill For Ore! / Thermal Boiler - Lava you long time / Electrum Flux Coil Upgrade
- [ ] L7278-L7280 (1) Helium is Not Just for Balloons
- [ ] L7286-L7332 (12) Playing With the Big Boys, Chemically / Better Glass Upgrade, EV Glass / IV Glass / LuV Glass / ZPM Glass / UV Glass … 他6件
- [ ] L7342-L7348 (2) Getting Muddy With Monazite / Dissolution Tank
- [ ] L7362-L7372 (3) Neutron Activator / Neutron Sensor / Neutron Accelerator
- [ ] L7390-L7412 (6) Focusing Science and Mystery / Catalyzing Miracles / Tier 2 Shielding / Tier 3 Shielding / Tier 4 Shielding / Too much Indium?
- [ ] L7418-L7448 (8) Algae Pond / Tier 2 Manipulating / A Beginner's Guide to Particle Physics / Producing Solar Panels in BULK!! / Synchrotron (No Relation to the Catalyst) / UXV Glass … 他2件
- [ ] L7454-L7476 (6) Don't ask how this works / Decay Warehouse / Don't Lose That Multiblock Miner! / Using That Algae / A Little More Sigma (Squared)⚠ / No More (IC) Engraving
- [ ] L7486-L7492 (2) Filtered Beamline Output Hatch / Component Assembly Line
- [ ] L7502-L7504 (1) Drones are not Drones!
- [ ] L7514-L7532 (5) Draconic Development / One Fluid Tank to Store it All!! / Tier 4 Manipulating / Tier 3 Manipulating / More Algae Uses

### 大量処理  _(L7535)_ — 未翻訳率: 57/66 (86%)

- [ ] L7543-L7673 (33) Big Beautiful Brewery / This Kinda Burns... / Mass Processing at UV and Beyond!⚠ / Fits The Mold / T2 Maceration Stack / Smelt All The Things Stack-Wise...⚠ … 他27件
- [ ] L7679-L7697 (5) MABS / Another Chemical Multiblock? / Mass Processing in LuV⚠ / Clean Implosions?! / Extraction Point
- [ ] L7703-L7717 (4) Insane Voltage Multiblocks / L.A.T.E.X. Cable Coater⚠ / The Form of the Former Former: Reformed⚠ / See You Lather
- [ ] L7727-L7773 (12) Taking Things Apart / Advanced Assembly Line / Advanced Autoclaving / Megalomania⚠ / ...With The Power of Science! / You've Gotta Keep 'Em Separated … 他6件
- [ ] L7779-L7781 (1) Thermic Heating Device⚠
- [ ] L7787-L7793 (2) Engraving With Style / Extreme Voltage Multiblocks

### 発電方法のハウ・トゥー  _(L7800)_ — 未翻訳率: 120/137 (88%)

- [ ] L7804-L7818 (4) Marie Curium? / XL Turbo Steam Turbine / Calcium Bottlenecking / Portable Clean Energy IV
- [ ] L7840-L7910 (18) Power of the Sun at MV Level / Power of the Sun 1x1 MV / Power of the Sun at HV Level / Power of the Sun 1x1 HV / We Need Big Toys / Power of the Sun at LV Level … 他12件
- [ ] L7916-L7938 (6) What Was That? I Can't Hear You Over the Engine! / Power of the Sun at EV Level / Power of the Sun 1x1 EV / Power of the Sun at IV Level / Power of the Sun 1x1 IV / Do You Hear That Engine Revving?
- [ ] L7948-L7954 (2) Fluid Regulator / Gas Turbine
- [ ] L7968-L8042 (19) Rocket Engine EV / Kinetic Wind Power EV / Kinetic Water Power IV / Kinetic Wind Power IV / Kinetic Water Power LuV / Power of the Sun at LuV Level … 他13件
- [ ] L8056-L8094 (10) You Haven't Learned How to Separate Fluids Yet? Seriously? / Acid Trip / Hallucinogenics Not Included / Portable Clean Energy EV / Portable Clean Energy LuV / Portable Clean Energy ZPM … 他4件
- [ ] L8100-L8206 (27) Radioisotope Thermoelectric Generator / Kinetic Power EV / Kinetic Power IV / Kinetic Power LuV / Kinetic Power ZPM / Kinetic Water Power EV … 他21件
- [ ] L8212-L8346 (34) Large Naquadah Reactor / Nuclear Based Fuel (Th) / Nuclear Based Fuel (U) / Nuclear Based Fuel (Pu) / Naquadah Fuel Refinery / Tier 2 Coil … 他28件

### EUの蓄電と変圧  _(L8349)_ — 未翻訳率: 46/63 (73%)

- [ ] L8353-L8363 (3) IV 16A Hatches / Can we get much higher? / Energized Wireless Dynamo Hatch
- [ ] L8405-L8415 (3) EV Battery Buffer / EV Sunnarium Battery / EV GT++ Batteries
- [ ] L8429-L8435 (2) Low Voltage Power Transformer / MV Battery Buffers
- [ ] L8441-L8547 (27) HV Battery Buffers / HV Battery Hulls / HV Battery / EU packets flowing everywhere... / Who Cares About a Little Cancer... / Lapotronic Energy Storage Unit … 他21件
- [ ] L8553-L8583 (8) Gotta Pump It Up / Let it flow, let it floww ... / Extremely Ultimate and Ultimately Extreme / Wireless Power!? / EV 4A Hatches / Power Goggles … 他2件
- [ ] L8589-L8599 (3) IV 4A Hatches / EV 16A Hatches / At last, the final capacitor!

### 石油のための労働  _(L8602)_ — 未翻訳率: 31/46 (67%)

- [ ] L8606-L8628 (6) Maxed Oil Cracker / Super Fuel At The Top / Breaking the Mold / Ultimate Distillation / Hyperheated Steam / Universal Fuel Power
- [ ] L8646-L8652 (2) The Era of Multis / Generator Power
- [ ] L8694-L8784 (23) Using All the Fractions / Oil Cracker / Boosting the Diesel / Special Rubber from Oil / Distilled Heavy Fuel / Acetone and Ethenone … 他17件

### 大衆("マス")のためのバイオ  _(L8787)_ — 未翻訳率: 34/48 (71%)

- [ ] L8831-L8833 (1) Biological Diesel
- [ ] L8839-L8889 (13) Pyrolyse Oven / Large Steel Boiler / Wood Tar / The Most Powerful Biodiesel / Trees Growing Faster / Sapling Power … 他7件
- [ ] L8895-L8925 (8) Green Nitric Acid / Green Ethenone / Green Cetane-Boosted Diesel / Fermented Biomass / Free For All Fertilizer / Methane Stinks … 他2件
- [ ] L8931-L8977 (12) Upgrading Your Benzene / CBD Into Steam / Mass Distilled Water / Nitric And Sulfuric Acid / Titanium Chemical Plant / Nitrobenzene … 他6件

### 原子核物理学は強力  _(L8980)_ — 未翻訳率: 34/57 (60%)

- [ ] L8988-L8990 (1) Focus on Breeding
- [ ] L9000-L9006 (2) Build the Assembly Line First / Improved Fission
- [ ] L9012-L9018 (2) The Path of Fusion / Building the Reactor
- [ ] L9036-L9062 (7) Focus On Power Generation / Liquid Fluorine Thorium Reactor / First Half of LFTR Breeding / Sparge Tower / Fusion Europium / How Much Power From One Reactor? … 他1件
- [ ] L9104-L9174 (18) Nuclear Fuel Processing / Inputs and Outputs in the LFTR / First Steps in Reprocessing / Second Half of LFTR Breeding / Faster Lutetium Excitement / Exciting Liquid Nuking … 他12件
- [ ] L9192-L9206 (4) Duranium and the Beam Crafter⚠ / Reactors are Expensive! / Establishment of Fusion / A Second Reactor?

### スペース・レース  _(L9209)_ — 未翻訳率: 122/141 (87%)

- [ ] L9217-L9247 (8) Can I Build A Mothership For My Father? / The Legs On The Shuttle Rocket Go Step, Step, Step... / Shuttle Nose Cone / A Reward / H8N4C2O4 (Green) Rocket Fuel / Load and Unload the Rocket … 他2件
- [ ] L9289-L9295 (2) Rocket Launch Pad / Gas 'Er Up
- [ ] L9313-L9327 (4) Oxygen Collector / Oxygen Compressor / Parachute / Advanced Wafers
- [ ] L9333-L9627 (74) 1,1-Dimethylhydrazine / Formaldehyde / Space Station / Are You Prepared? / Moon Arrival / Ceres Dungeon … 他68件
- [ ] L9633-L9715 (21) Coal Tar Distilling / Dense Hydrazine / Monomethylhydrazine / CN3H7O3 (Purple) Rocket Fuel / 2-Ethylanthrahydroquinone / 2-Ethylanthraquinone … 他15件
- [ ] L9721-L9771 (13) Proteus Dungeon / Tier 6 Control Computer / Enceladus Dungeon / Space Pumping / How Do I Charge This Stuff?⚠ / steve@mothership:~$ … 他7件

### 基本的な自動化  _(L9774)_ — 未翻訳率: 15/35 (43%)

- [ ] L9782-L9832 (13) Cart Modules: Coal Power / Automated (un-)Loading / Cart Modules: Farming / Cart Modules: Storage / A Simple Cart / Cart Modules: Wood Cutter … 他7件
- [ ] L9902-L9904 (1) Dealing with H2S
- [ ] L9910-L9912 (1) Reward for Desulfurizing Automation

### SFMとコンピューター  _(L9915)_ — 未翻訳率: 53/54 (98%)

- [ ] L9919-L10129 (53) It's everytime these Transistors / Welcome to OpenComputers! / Your First Microchip / Your First Computer / Arithmetic Logic Circuits / All Your Card Are Belong To Us … 他47件

### パイプでロジスティクス  _(L10132)_ — 未翻訳率: 8/31 (26%)

- [ ] L10172-L10178 (2) Sorting Incoming / More ItemSinks in NEI
- [ ] L10188-L10194 (2) There Is Extra Stuff... / Remote requests
- [ ] L10208-L10210 (1) Time to See The Process
- [ ] L10220-L10222 (1) It's DA BEST
- [ ] L10240-L10242 (1) Modular Upgrades
- [ ] L10248-L10250 (1) I NEED THAT!!!!!!

### Applied Energistics  _(L10257)_ — 未翻訳率: 181/185 (98%)

- [ ] L10261-L10297 (9) 1024k Essentia Component / AE Tier 2 Fluid Storage / Quantum Entangled Singularities / Cribs / Need More Information? / 16384k Fluid Component … 他3件
- [ ] L10303-L10305 (1) 16k Item Storage Cell
- [ ] L10311-L10381 (18) Applied Crafting / Getting Your First Processors / Cables / Basic Terminals / Bundled AE Channels / Quantum Storage … 他12件
- [ ] L10387-L10841 (114) Keeping Your Network Happy / Storing Your ME Data / Speeding Up Growth / Perfecting Crystal Growth / Purifying the Impure / Maximum Security⚠ … 他108件
- [ ] L10847-L11001 (39) Co-Processing x256⚠ / 4096k Essentia Storage Cell / Get Your Priorities Straight / 16384k Essentia Component / Hyper Acceleration! / Advanced Neutronium Tech … 他33件

### 養蜂要領を守って  _(L11004)_ — 未翻訳率: 43/83 (52%)

- [ ] L11008-L11010 (1) The Truth About Serum⚠
- [ ] L11016-L11020 (1) Top-Tier Analyzer
- [ ] L11046-L11170 (21) Mutatron / Genetic Sampler / Diamondware / Genetic Imprinter / Genetic Transposer / Advanced Mutatron … 他15件
- [ ] L11228-L11232 (1) Breeding Bees Into Oblivion⚠
- [ ] L11258-L11262 (1) Fastest Way to Get There
- [ ] L11280-L11308 (5) Genepool / Isolator / Sequencer / Polymeriser / Gene Database
- [ ] L11314-L11324 (2) Registry / Droning On⚠
- [ ] L11338-L11342 (1) Keep Calm and Bee On
- [ ] L11348-L11352 (1) Bee Slurry, the Breakfast of, Well, Weirdos
- [ ] L11362-L11378 (3) A Bag for Butterflies, yawn / Only the Best: Tree Breeding / Only the Worst: Trees Suck!
- [ ] L11384-L11410 (6) IAADDS / Pollen Collection Kit / Living It Larvae⚠ / Fluorescent Dye / Enzyme on The Mind⚠ / Growth Medium

### 交配の方蜂(ほうほう)  _(L11413)_ — 未翻訳率: 59/189 (31%)

- [ ] L11417-L11419 (1) MakeMake
- [ ] L11437-L11439 (1) Iridium
- [ ] L11445-L11447 (1) Neutronium
- [ ] L11457-L11459 (1) Naquadah
- [ ] L11477-L11479 (1) Gassy Bees
- [ ] L11509-L11515 (2) End Dust / Indium
- [ ] L11521-L11523 (1) Dragon Blood
- [ ] L11585-L11599 (4) Batty / Ghastly / Smouldering / Refined
- [ ] L11641-L11643 (1) Sandwich
- [ ] L11701-L11703 (1) Oil
- [ ] L11813-L11815 (1) Zinc
- [ ] L11837-L11839 (1) Titanium
- [ ] L11849-L11851 (1) Uranium
- [ ] L11917-L11919 (1) Aer
- [ ] L11937-L11943 (2) Spirit / Soul
- [ ] L11957-L11963 (2) Rejuvenating / Empowering
- [ ] L11973-L11975 (1) Thaumium Dust
- [ ] L11985-L11987 (1) Thaumic Shards
- [ ] L12001-L12019 (5) Abandoned / Draconic / Wither / Withering / Spiteful
- [ ] L12037-L12047 (3) D-O-B / Ender Shard / Nether Shard
- [ ] L12053-L12151 (25) Energium / Attuned⚠ / Uranus⚠ / Moon / Salt⚠ / Barnarda⚠ … 他19件
- [ ] L12163-L12169 (2) Oberon / Infinity Catalyst

### Hardcore End(er) Expansion  _(L12172)_ — 未翻訳率: 40/40 (100%)

- [ ] L12176-L12334 (40) Spatial Distortions / Dimensional Chest / Is This the End? No, it's the END Dimension⚠ / Ender Towers / Welcome to the End! / Dragon Essence Altar⚠ … 他34件

### 初歩的な魔導学  _(L12337)_ — 未翻訳率: 51/102 (50%)

- [ ] L12341-L12351 (3) The Choice: Ordo / The Choice: Aqua / The Choice: Aer
- [ ] L12357-L12359 (1) Witchy (Wo)man
- [ ] L12381-L12383 (1) Tome of Knowledge
- [ ] L12409-L12411 (1) Fuuuuuu...(sion)!
- [ ] L12433-L12459 (7) The Choice: Ignis / The Choice... / The Choice: Terra / The Choice: Perditio / This is the End... / Turning Liquids Into Essentia … 他1件
- [ ] L12473-L12487 (4) Infinite... Lava? / Infinite Water! / Improved Armor: Samurai Style / A New Way to "Farm" Resources
- [ ] L12493-L12495 (1) Enchanted Earth
- [ ] L12501-L12507 (2) Gold-Banded Greatwood Scepter / Primal Charm
- [ ] L12525-L12531 (2) Division Sigil / Cursed Earth
- [ ] L12537-L12539 (1) Blub Blub Blub.....
- [ ] L12573-L12575 (1) The Night's Not Dark Anymore
- [ ] L12581-L12583 (1) So Thirsty
- [ ] L12593-L12595 (1) 3 Plus 4, Carry the 2...
- [ ] L12605-L12607 (1) Boots Are Made For Walking
- [ ] L12613-L12619 (2) Infinite Bats! Wait, What?? / Greedy Chest
- [ ] L12629-L12631 (1) Everything Fuzzy? Try Some Lenses
- [ ] L12637-L12675 (10) Gimme gimme gimme / It's Called the Thaumatorium, OK? / Growing Auram / Thauminite Helmet / The Burden of Knowledge / Comparing at a Distance … 他4件
- [ ] L12689-L12695 (2) Need More Sugar? / Thaumic Dendrology⚠
- [ ] L12701-L12707 (2) Pushing Back the Taint / Adding More Functions
- [ ] L12717-L12743 (7) Growing your own Knowledge! / Solid, Directional Redstone / Alleviating Warp / Counting Items / Magical Plants⚠ / Tube Madness … 他1件

### 発展的な魔導学  _(L12746)_ — 未翻訳率: 76/78 (97%)

- [ ] L12750-L12976 (57) Smoke Your Normal Warp Away / Adept Thaumaturgy / An Awesome Magic Conductor / A Silverwood Wand at Last / Creating a Better Wand / More Energetic Screws to Finish the New Wand … 他51件
- [ ] L12982-L13056 (19) Healing Your Nodes / Disenchanted / Fool's Gold / Gen XXXXXXXXXX... / Purge...Some of Your Warp? / Essentia Transmission … 他13件

### カーミー、ハーミー、...波ァ！  _(L13059)_ — 未翻訳率: 36/37 (97%)

- [ ] L13063-L13205 (36) Lord of the Rings? / The Power of Gods / Shards of Opposite Worlds / Unleashed the Power - Cowl / Unbreakable Cowl / Unleashed the Power - Leggings … 他30件

### 杖の杖星とEMT  _(L13208)_ — 未翻訳率: 38/40 (95%)

- [ ] L13212-L13250 (10) An Appropriate Weapon / Dropped in Asgard, Fallen to Earth / Repaired it! / Super-Mjolnir / Sparking Nitor...? / Rechargeable Scribing Tools … 他4件
- [ ] L13256-L13366 (28) I Don't Want to Set the World on Fire / Diggy Diggy Hole / Bzzap! / Trade Offer / Snowball Fight! / Magical Base Defense … 他22件

### 花の力  _(L13369)_ — 未翻訳率: 27/44 (61%)

- [ ] L13373-L13375 (1) Fountain Of Conjuration
- [ ] L13409-L13435 (7) A Glimpse Into A Watery Future / Botanic Infusion / Terrasteel / Alfheim / Round One... FIGHT! / A Deal With Alfar Industries … 他1件
- [ ] L13469-L13543 (19) Anti-Magnetism / Violence Is Blue / Roses Are Blood-Red / Magic Blue Dust / Better Generating Flowers / Shut Down Your Canning Machine … 他13件

### "端"に目を向ける  _(L13546)_ — 未翻訳率: 91/93 (98%)

- [ ] L13550-L13644 (24) Fire Burn and... / Offerings / ...Cauldron Bubble / Don't Touch the Needle! / Probably Usable For Soup / Don't Shake it Too Much … 他18件
- [ ] L13650-L13916 (67) Purified Milk / Brew of Love / Sleep Well! / The Spirit World - Nightmare / Early Bird Gets the...Nightmare? / Wake Up Early … 他61件

### 高い対価を払って  _(L13919)_ — 未翻訳率: 73/74 (99%)

- [ ] L13923-L14213 (73) Incense Crucible / Tier 2 Sigils / Paying the Highest Price / Portable Battery... / Poke / Tier 3 Sigils … 他67件

### 全部ブッ殺せ  _(L14216)_ — 未翻訳率: 153/344 (44%)

- [ ] L14220-L14254 (9) Time To Kill (Crimson Knight)⚠ / Kill Baba Yaga / Kill Horned Huntsman / Kill Ender Dragon / Kill Shade of Leonard / Kill Lord of Tormentum … 他3件
- [ ] L14264-L14274 (3) Slay the Eyes! / Ender Guardians / Slay the Dragon. (Again)
- [ ] L14416-L14430 (4) Time to Kill (Fire Golem) / Time to kill (Haunted Miners) / Time to Kill (Louse) / Time to Kill (Scorching Lens)
- [ ] L14555-L14565 (3) Something From Nothing Pt 2 / Industrial Water Purification / Waterproof Tech
- [ ] L14571-L14581 (3) Integrated Ore Factory - All in One! / Proto-Volt Stabilizer⚠ / Streamlined Casters⚠
- [ ] L14619-L14625 (2) Dark Steel Tools / And It Will Never Break
- [ ] L14635-L14637 (1) Monitoring Your Reactor
- [ ] L14655-L14665 (3) Magical Waystones / Industrial 3D Copying Machine / Draconic Evolution
- [ ] L14711-L14717 (2) Advanced Nano Chestplate / Gravi Suit
- [ ] L14723-L14729 (2) Dark Steel Tool and Weapon Basic Upgrades / Dark Steel Tool and Weapon Advanced Upgrades
- [ ] L14759-L14761 (1) Power of the Sun ULV
- [ ] L14779-L14781 (1) Moron's Guide to Better Trees
- [ ] L14835-L14841 (2) Making Power With Your Plasma / Turbine Time
- [ ] L14875-L14881 (2) Need a Place For All Those Ores? / Angel Wings - Combine!
- [ ] L14887-L14905 (5) Pimp Your Wand Focus / Mallard Rust Smelly / Shake That Booty... / Launch Controller / Arc Lamp
- [ ] L14955-L14957 (1) Planetary Tears
- [ ] L14963-L14965 (1) Don't Put a Finger in That Socket
- [ ] L14983-L14993 (3) Too Much Mercury? / I'll Send Wireless Signals Where I Want, Thank You / Wireless 3.0
- [ ] L15011-L15041 (8) Unlimited LP / Infinity Chest / UV Solar / Does Anyone Even Still Use These? / Transform and...Stay Put Actually / What Even is This? … 他2件
- [ ] L15047-L15049 (1) 「 」
- [ ] L15055-L15097 (11) Nano Forge Tier 2 / Nano Forge Tier 3 / Chemical Pseudo-Altercations / Precise Assembler / Industrial Coke Oven / Bet On The Distillus … 他5件
- [ ] L15103-L15165 (16) Eternal Coil Upgrade / Power in the Ether / PCB Factory / Bio Chamber / Liquid Cooling Tower / PCB Factory Tier 2 … 他10件
- [ ] L15171-L15181 (3) Heliocast Reinforcement⚠ / Balance is Everything / Celestial Gateways
- [ ] L15187-L15189 (1) Large Molecular Assembler
- [ ] L15195-L15201 (2) Sentient Overclocker⚠ / Large Hadron Collider
- [ ] L15215-L15237 (6) The Quest for Holy Water / High Energy Laser Purification / Neutronium Compressor / Matter Manipulator MKI / Universal Collapser⚠ / Matter Manipulator MKIII
- [ ] L15247-L15261 (4) Absolute Purity / Crafting Input Proxy / The Everlasting Guilty Pool / pH Neutralization
- [ ] L15267-L15277 (3) Hypercooler⚠ / Multiblock Revolution / Nano Forge Tier 4
- [ ] L15283-L15289 (2) Never Hungry Again / Quantum Uplink
- [ ] L15295-L15297 (1) Clarifier
- [ ] L15303-L15305 (1) Purifying Water With Plasma
- [ ] L15311-L15313 (1) Flocculation
- [ ] L15319-L15333 (4) Crafting, but with Beams!⚠ / Thaumometric Essentia Cell / Creative Mana Tablet / Exo-Foundry⚠
- [ ] L15338-L15364 (7) Trigger: Nano Boots of the Traveller Skip / Trigger: Runeforged Thaumaturge's Ring / Trigger: Nightvision Goggle Skip / Trigger: Hafnium Skip / Trigger: Rocket Shuttle Skip / Trigger: Naquadria Skip … 他1件
- [ ] L15398-L15400 (1) Bees Template
- [ ] L15426-L15428 (1) Trigger: Flippers
- [ ] L15470-L15532 (16) Tool: Never complete / Trigger: NaK Skip / Trigger: Dense Hydrazine Skip / Trigger: Zirconium Skip / Trigger: Netherite Skip / Trigger: Cerium Skip … 他10件
- [ ] L15538-L15572 (9) Trigger: Rocket Tier 2 Skip / Trigger: SMD Inductor Skip / Trigger: Division Sigil / Trigger: Polyphenylene Sulfide Skip / Trigger: Rocket Tier 7 Skip / Trigger: Profane Wand … 他3件
- [ ] L15578-L15604 (7) Trigger: Prismarine Line Skip / Trigger: CN3H7O3 (Purple) Rocket Fuel Skip / Ice Cream Trophy⚠ / Trigger: Oblivion Frame / Trigger: Rocket Tier 6 Skip / Trigger: Stonelily Tutorial Skip⚠ … 他1件

## 要注意: バージョン差異で翻訳作業を保留(137件)

上のブロック一覧にも含まれるが、2.8.4実機のゲーム内で翻訳を確認できないため、
いま翻訳作業はせず、対象クエストが実装されて確認できるようになってから着手する。

- L1424 Void Buses — v2.9新規(2.8.4に無くゲーム内未確認)
- L1985 MV Wiremill — v2.9新規(2.8.4に無くゲーム内未確認)
- L1989 MV Cutting Machine — v2.9新規(2.8.4に無くゲーム内未確認)
- L1993 Dislocator Inhibitor — v2.9新規(2.8.4に無くゲーム内未確認)
- L1997 String Theory? — v2.9新規(2.8.4に無くゲーム内未確認)
- L2001 Still No Filing in MV — v2.9新規(2.8.4に無くゲーム内未確認)
- L2022 Personal Dimension — ID使い回し(2.8.4「Reward choice: Personal Dimension」→2.9「§5§lPersonal Dimension」ゲーム内未確認)
- L2426 Fluoro-who now? — v2.9新規(2.8.4に無くゲーム内未確認)
- L2430 Melting and Refreezing — v2.9新規(2.8.4に無くゲーム内未確認)
- L2904 Chemical Reactions at IV Level — ID使い回し(2.8.4「§b§lChemical Reactions at IV level」→2.9「§9§lChemical Reactions at IV Level」ゲーム内未確認)
- L3461 Imprint Supporting Boards — ID使い回し(2.8.4「§c§lRNG is Definitely Good Game Design」→2.9「§d§lImprint Supporting Boards」ゲーム内未確認)
- L3854 Wormhole Generator — v2.9新規(2.8.4に無くゲーム内未確認)
- L4059 Elastic Singularity — v2.9新規(2.8.4に無くゲーム内未確認)
- L4221 NAC™: Advanced Routing Package — v2.9新規(2.8.4に無くゲーム内未確認)
- L4305 NAC™: Crystal Package — v2.9新規(2.8.4に無くゲーム内未確認)
- L4325 NAC™: Wetware and Bioware Package — v2.9新規(2.8.4に無くゲーム内未確認)
- L4377 NAC™: Automation Package — v2.9新規(2.8.4に無くゲーム内未確認)
- L4393 Biocatalyzed Propulsion Fluid — v2.9新規(2.8.4に無くゲーム内未確認)
- L4397 NAC™: Optical Package — v2.9新規(2.8.4に無くゲーム内未確認)
- L4405 NAC™: Assembling Package — v2.9新規(2.8.4に無くゲーム内未確認)
- L4413 UEV Field Generator — v2.9新規(2.8.4に無くゲーム内未確認)
- L4421 Using... Goop To Compute? — v2.9新規(2.8.4に無くゲーム内未確認)
- L4450 Dyson Swarm Modules — v2.9新規(2.8.4に無くゲーム内未確認)
- L4490 Six-Phased Copper — v2.9新規(2.8.4に無くゲーム内未確認)
- L4502 A Diode, But For Condensate — v2.9新規(2.8.4に無くゲーム内未確認)
- L4567 Energised Tesseract — v2.9新規(2.8.4に無くゲーム内未確認)
- L4607 Maybe I Do Need These — v2.9新規(2.8.4に無くゲーム内未確認)
- L4640 Zepto Power IC — v2.9新規(2.8.4に無くゲーム内未確認)
- L4672 Resplendent Components — v2.9新規(2.8.4に無くゲーム内未確認)
- L4688 Reinforced Components — v2.9新規(2.8.4に無くゲーム内未確認)
- L4696 Perfected Components — v2.9新規(2.8.4に無くゲーム内未確認)
- L4704 T7: Perfect — v2.9新規(2.8.4に無くゲーム内未確認)
- L4712 A Solder Singularity — v2.9新規(2.8.4に無くゲーム内未確認)
- L4716 T2: Primitive — v2.9新規(2.8.4に無くゲーム内未確認)
- L4752 T8: Tipler — v2.9新規(2.8.4に無くゲーム内未確認)
- L4768 Refined Components — v2.9新規(2.8.4に無くゲーム内未確認)
- L4784 T5: Superb — v2.9新規(2.8.4に無くゲーム内未確認)
- L4797 A Universe In Your Drives — v2.9新規(2.8.4に無くゲーム内未確認)
- L4805 Strings Upon Strings Upon Strings Upon- — v2.9新規(2.8.4に無くゲーム内未確認)
- L4833 You'll Only Need a Few of These — ID使い回し(2.8.4「You'll Probably Need Quite a Few of These」→2.9「§6§l§nYou'll Only Need a Few of These」ゲーム内未確認)
- L4849 UXV Energy Hatch — v2.9新規(2.8.4に無くゲーム内未確認)
- L4897 A Minor Roadblock — v2.9新規(2.8.4に無くゲーム内未確認)
- L5102 Ice Ice Baby — v2.9新規(2.8.4に無くゲーム内未確認)
- L6289 Compressed Titanium Armor — ID使い回し(2.8.4「Compressed Titan Armor」→2.9「Compressed Titanium Armor」ゲーム内未確認)
- L6381 Eldritch Striders — v2.9新規(2.8.4に無くゲーム内未確認)
- L6389 Apprentice Striders — v2.9新規(2.8.4に無くゲーム内未確認)
- L6430 Barrel Upgrades — v2.9新規(2.8.4に無くゲーム内未確認)
- L6650 Chests Had Quite the Glow-up! — v2.9新規(2.8.4に無くゲーム内未確認)
- L6726 Marking Your Base — v2.9新規(2.8.4に無くゲーム内未確認)
- L7442 Stern-Gerlach, Perhaps? — v2.9新規(2.8.4に無くゲーム内未確認)
- L7470 A Little More Sigma (Squared) — v2.9新規(2.8.4に無くゲーム内未確認)
- L7551 Mass Processing at UV and Beyond! — v2.9新規(2.8.4に無くゲーム内未確認)
- L7563 Smelt All The Things Stack-Wise... — ID使い回し(2.8.4「Smelt All the Things Stack-Wise...」→2.9「§5§lSmelt All The Things Stack-Wise...」ゲーム内未確認)
- L7571 A Volcano For Your Base. — ID使い回し(2.8.4「A volcano for your base.」→2.9「§9§lA Volcano For Your Base.」ゲーム内未確認)
- L7587 The Rocks In The Washer... — ID使い回し(2.8.4「The rocks in the washer...」→2.9「§8§lThe Rocks In The Washer...」ゲーム内未確認)
- L7591 Dancing In Circles — ID使い回し(2.8.4「Dancing in circles」→2.9「§8§lDancing In Circles」ゲーム内未確認)
- L7595 I Think I'm Going to be Sick — ID使い回し(2.8.4「I think I'm going to be sick」→2.9「§8§lI Think I'm Going to be Sick」ゲーム内未確認)
- L7599 Bask In The Currents — ID使い回し(2.8.4「Bask in the currents」→2.9「§9§lBask In The Currents」ゲーム内未確認)
- L7607 Play-Doh For Big Girls and Boys — ID使い回し(2.8.4「Play doh for big girls and boys」→2.9「§9§lPlay-Doh For Big Girls and Boys」ゲーム内未確認)
- L7611 Best Thing Since Sliced Bread — ID使い回し(2.8.4「Best thing since sliced bread」→2.9「§9§lBest Thing Since Sliced Bread」ゲーム内未確認)
- L7627 Spools and Spools — ID使い回し(2.8.4「Spools and spools」→2.9「§9§lSpools and Spools」ゲーム内未確認)
- L7631 Bender, More Bending! — ID使い回し(2.8.4「Bender more bending」→2.9「§8§lBender, More Bending!」ゲーム内未確認)
- L7635 Bezos Would Be Proud — ID使い回し(2.8.4「Bezos would be proud」→2.9「§9§lBezos Would Be Proud」ゲーム内未確認)
- L7647 Empty The Oceans — ID使い回し(2.8.4「Empty the oceans」→2.9「§9§lEmpty The Oceans」ゲーム内未確認)
- L7651 Putting All Those Workers Out of Jobs — ID使い回し(2.8.4「Putting all those workers out of jobs」→2.9「§b§lPutting All Those Workers Out of Jobs」ゲーム内未確認)
- L7663 Cool Guys Don't Look At Explosions — ID使い回し(2.8.4「Cool Guys Don't Look at Explosions」→2.9「§9§lCool Guys Don't Look At Explosions」ゲーム内未確認)
- L7667 Let Me Fabricate a New Universe... — ID使い回し(2.8.4「Let me fabricate a new universe...」→2.9「§b§lLet Me Fabricate a New Universe...」ゲーム内未確認)
- L7671 I Want SOLIDS Not LIQUIDS! — ID使い回し(2.8.4「I Want SOLIDS not LIQUIDS!」→2.9「§9§lI Want SOLIDS Not LIQUIDS!」ゲーム内未確認)
- L7687 Mass Processing in LuV — ID使い回し(2.8.4「Mass Processing in LuV and Beyond」→2.9「§d§lMass Processing in LuV」ゲーム内未確認)
- L7707 L.A.T.E.X. Cable Coater — v2.9新規(2.8.4に無くゲーム内未確認)
- L7711 The Form of the Former Former: Reformed — v2.9新規(2.8.4に無くゲーム内未確認)
- L7739 Megalomania — v2.9新規(2.8.4に無くゲーム内未確認)
- L7759 Can It! — ID使い回し(2.8.4「Can it!」→2.9「§5§lCan It!」ゲーム内未確認)
- L7763 Spinmatron-2737 — v2.9新規(2.8.4に無くゲーム内未確認)
- L7779 Thermic Heating Device — v2.9新規(2.8.4に無くゲーム内未確認)
- L8774 Higher Capacity Dynamo — ID使い回し(2.8.4「Buffered Dynamo」→2.9「Higher Capacity Dynamo」ゲーム内未確認)
- L9192 Duranium and the Beam Crafter — ID使い回し(2.8.4「Duranium and the Cyclotron」→2.9「Duranium and the Beam Crafter」ゲーム内未確認)
- L9737 How Do I Charge This Stuff? — ID使い回し(2.8.4「How the Eff Do I Charge This Sh*t?」→2.9「How Do I Charge This Stuff?」ゲーム内未確認)
- L10287 Pattern Repeater — v2.9新規(2.8.4に無くゲーム内未確認)
- L10407 Maximum Security — ID使い回し(2.8.4「Wireless Setup」→2.9「Maximum Security」ゲーム内未確認)
- L10559 Easier AL Automation — ID使い回し(2.8.4「Easier AL automation」→2.9「Easier AL Automation」ゲーム内未確認)
- L10847 Co-Processing x256 — v2.9新規(2.8.4に無くゲーム内未確認)
- L10899 Co-Processing x1024 — v2.9新規(2.8.4に無くゲーム内未確認)
- L10923 Advanced Level Emitter — v2.9新規(2.8.4に無くゲーム内未確認)
- L10943 Co-Processing x64 — v2.9新規(2.8.4に無くゲーム内未確認)
- L10951 Certified Geek, 7 Days a Week — v2.9新規(2.8.4に無くゲーム内未確認)
- L10987 Co-Processing x4096 — v2.9新規(2.8.4に無くゲーム内未確認)
- L11008 The Truth About Serum — v2.9新規(2.8.4に無くゲーム内未確認)
- L11228 Breeding Bees Into Oblivion — ID使い回し(2.8.4「Bees Buzzing Beyond the Dark」→2.9「Breeding Bees Into Oblivion」ゲーム内未確認)
- L11320 Droning On — ID使い回し(2.8.4「Inoculator」→2.9「Droning On」ゲーム内未確認)
- L11396 Living It Larvae — v2.9新規(2.8.4に無くゲーム内未確認)
- L11404 Enzyme on The Mind — v2.9新規(2.8.4に無くゲーム内未確認)
- L12057 Attuned — v2.9新規(2.8.4に無くゲーム内未確認)
- L12061 Uranus — v2.9新規(2.8.4に無くゲーム内未確認)
- L12069 Salt — v2.9新規(2.8.4に無くゲーム内未確認)
- L12073 Barnarda — v2.9新規(2.8.4に無くゲーム内未確認)
- L12081 Infinity — v2.9新規(2.8.4に無くゲーム内未確認)
- L12085 Infernal — v2.9新規(2.8.4に無くゲーム内未確認)
- L12089 Trinium — v2.9新規(2.8.4に無くゲーム内未確認)
- L12105 Oriharukon — v2.9新規(2.8.4に無くゲーム内未確認)
- L12113 Enceladus — v2.9新規(2.8.4に無くゲーム内未確認)
- L12117 Saturn — v2.9新規(2.8.4に無くゲーム内未確認)
- L12121 Barnarda F — v2.9新規(2.8.4に無くゲーム内未確認)
- L12129 Pluto — v2.9新規(2.8.4に無くゲーム内未確認)
- L12133 Neptune — v2.9新規(2.8.4に無くゲーム内未確認)
- L12141 Mars — v2.9新規(2.8.4に無くゲーム内未確認)
- L12149 Jupiter — v2.9新規(2.8.4に無くゲーム内未確認)
- L12184 Is This the End? No, it's the END Dimension — ID使い回し(2.8.4「Is This the End? No it's the END Dimension」→2.9「Is This the End? No, it's the END Dimension」ゲーム内未確認)
- L12196 Dragon Essence Altar — ID使い回し(2.8.4「Essence Altar Dragon Infused」→2.9「Dragon Essence Altar」ゲーム内未確認)
- L12216 Visit the (Enchanted) Laboratory Island — ID使い回し(2.8.4「Visit the Laboratory Island」→2.9「Visit the (Enchanted) Laboratory Island」ゲーム内未確認)
- L12220 Energy Clusters and the Energy Wand — ID使い回し(2.8.4「Energy Wand」→2.9「Energy Clusters and the Energy Wand」ゲーム内未確認)
- L12224 Visit the (Enchanted) Homeland Island — ID使い回し(2.8.4「Visit the Enchanted Island」→2.9「Visit the (Enchanted) Homeland Island」ゲーム内未確認)
- L12669 Timewood Tree — v2.9新規(2.8.4に無くゲーム内未確認)
- L12693 Thaumic Dendrology — v2.9新規(2.8.4に無くゲーム内未確認)
- L12733 Magical Plants — v2.9新規(2.8.4に無くゲーム内未確認)
- L13022 Primordial Armor — v2.9新規(2.8.4に無くゲーム内未確認)
- L13030 Infused Seeds — v2.9新規(2.8.4に無くゲーム内未確認)
- L13191 Runeforged Thaumaturge's Ring — v2.9新規(2.8.4に無くゲーム内未確認)
- L13195 Master Earth Rings — v2.9新規(2.8.4に無くゲーム内未確認)
- L13199 Ring of the Sky — v2.9新規(2.8.4に無くゲーム内未確認)
- L14203 Ritual of Gaia's Transformation — v2.9新規(2.8.4に無くゲーム内未確認)
- L14220 Time To Kill (Crimson Knight) — ID使い回し(2.8.4「Secrets」→2.9「Time To Kill (Crimson Knight)」ゲーム内未確認)
- L14575 Proto-Volt Stabilizer — v2.9新規(2.8.4に無くゲーム内未確認)
- L14579 Streamlined Casters — v2.9新規(2.8.4に無くゲーム内未確認)
- L15079 Faster Basic Crops — ID使い回し(2.8.4「§6§lFaster Crops」→2.9「§6§lFaster Basic Crops」ゲーム内未確認)
- L15087 High Temperature Gas-cooled Reactor — ID使い回し(2.8.4「§6§lHigh Temperature Super Breeder」→2.9「§6§lHigh Temperature Gas-cooled Reactor」ゲーム内未確認)
- L15127 Liquid Cooling Tower Tier 2 — ID使い回し(2.8.4「Thermosink Radiator」→2.9「§c§l§nLiquid Cooling Tower Tier 2」ゲーム内未確認)
- L15159 Superdense Casting Basins — v2.9新規(2.8.4に無くゲーム内未確認)
- L15171 Heliocast Reinforcement — v2.9新規(2.8.4に無くゲーム内未確認)
- L15195 Sentient Overclocker — v2.9新規(2.8.4に無くゲーム内未確認)
- L15231 Universal Collapser — v2.9新規(2.8.4に無くゲーム内未確認)
- L15267 Hypercooler — v2.9新規(2.8.4に無くゲーム内未確認)
- L15319 Crafting, but with Beams! — v2.9新規(2.8.4に無くゲーム内未確認)
- L15331 Exo-Foundry — v2.9新規(2.8.4に無くゲーム内未確認)
- L15526 Trigger: Air-Filter — v2.9新規(2.8.4に無くゲーム内未確認)
- L15586 Ice Cream Trophy — v2.9新規(2.8.4に無くゲーム内未確認)
- L15598 Trigger: Stonelily Tutorial Skip — v2.9新規(2.8.4に無くゲーム内未確認)


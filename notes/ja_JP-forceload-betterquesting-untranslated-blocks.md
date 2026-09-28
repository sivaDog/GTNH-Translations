# ja_JP forceload/betterquesting 未翻訳ブロック一覧

対象ファイル: `ja_JP/config/txloader/forceload/betterquesting/lang/ja_JP.lang`
生成日: 2026-09-28

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
- L5226 Weed-EX
- L6505 Botany
- L6641 Carpenter's Blocks
- L10276 Applied Energistics
- L12191 Hardcore End(er) Expansion
- L14886 Better Questing?
- L15453 Trigger: Loot Game

## バージョン差異による除外(3件)

2.8.4のクエストDBにのみ存在し、v2.9(master)では削除されているクエスト。
この資料には載せず、翻訳作業の対象にもしない。

- L15644 [下書き]遺伝学者の道具
- L15647 [下書き]分析機
- L15650 [下書き]接続機

## サマリー

- ファイル内の全クエスト/クエストライン数: 3863(誤検出・バージョン差異除外後 3845)
- 未翻訳率: 2120/3845 (55%)
  - うち `[下書き]` 表記(未訳扱い): 63件
  - うち ⚠バージョン差異で翻訳作業を保留: 137件
- 連続ブロック数: 246

## 進捗(前回資料生成からの差分)

基準: 前回資料生成時点(2026-09-22) との比較。

- この基準以降に翻訳が完了したクエスト: 12件
- この基準以降に新規追加された未翻訳クエスト(フォーク元の更新等): 4件

翻訳完了したクエスト一覧:

- L11936 Aer
- L12428 Fuuuuuu...(sion)!
- L12474 Turning Liquids Into Essentia
- L12480 Essentia Filtering
- L12518 Enchanted Earth
- L12608 So Thirsty
- L12646 Greedy Chest
- L12680 Thauminite Helmet
- L12694 Taint Warnings
- L12736 Pushing Back the Taint
- L12758 Solid, Directional Redstone
- L15302 Multiblock Revolution

新規追加された未翻訳クエスト一覧:

- L4570 Eternal Coil Upgrade
- L6441 Texturing made easy
- L6733 Cooper's Mallet
- L15505 Trigger: Quantum Armor Skip

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

### Tier 7 - ZPM時代  _(L3630)_ — 未翻訳率: 50/66 (76%)

- [ ] L3634-L3640 (2) Prismatic Naquadah Composite Slurry / Prismatic Acid
- [ ] L3686-L3712 (7) Energy Infuser / Quantum Anomaly / Fusion Reactor MKII - Bigger, Better, Fusor / Making Americium / Learning Curve? Where We're Going There Are No Curves / The Beginning of the End Game … 他1件
- [ ] L3718-L3792 (19) You Can't Get Enough of This Pt 2 in ZPM / ZPM Superconductors (131,072 EU/t) / ZPM Field Generator / ZPM Assembler / ZPM Energy Hatch / Europium Doped Wafers … 他13件
- [ ] L3798-L3832 (9) Concentration / Recycle Trinium / Linear Accelerator / Refining / N.N.Q.Q.N.Q.Q / Purification … 他3件
- [ ] L3842-L3892 (13) Prismarine Recycling Pt. 2 / Prismarine Solution / Prismarine!? What Do I Need That For? / Prismatic Gas / Wormhole Generator⚠ / Naquarite Universal Insulator Foil … 他7件

### Tier 8 - UV時代  _(L3895)_ — 未翻訳率: 41/43 (95%)

- [ ] L3903-L4065 (41) I Put Fusion in Your Fusion so you Can Fusion While You Fusion / Time for Another Reactor / Americium Doped Wafers / Quantum Computer / Research Station / Maintenance Free At Last! … 他35件

### Tier 9 - UHV時代  _(L4068)_ — 未翻訳率: 29/33 (88%)

- [ ] L4072-L4078 (2) Draconic Core / Wyvern Core
- [ ] L4084-L4094 (3) Infinite Vis Storage, kinda? / Infinite Oxygen Tank / Misc Endgame Goals
- [ ] L4108-L4202 (24) UHV Superconductors (2,097,152 EU/t) / UHV Field Generator / UHV Energy Hatch / Assembling Living Circuits / The Final Frontier? / It's Not Going Bad, I Swear! … 他18件

### Tier 10 - UEV時代  _(L4205)_ — 未翻訳率: 53/55 (96%)

- [ ] L4209-L4267 (15) Capturing Light on a Circuit Board / Stopping the Infinity Bleed / My Eyes Hurt! #2 / NAC™: Advanced Routing Package⚠ / NAC™: Fundamentals Package / Awakened Core … 他9件
- [ ] L4273-L4423 (38) Longbow of the Heavens / My Eyes Hurt! #4 / Tesseract / Dragonblood / Metastable Oganesson / Infinity Boots … 他32件

### Tier 11 - UIV時代  _(L4426)_ — 未翻訳率: 46/47 (98%)

- [ ] L4430-L4612 (46) Bending Space and Time / Quantum Tank X / Heliofusion Exoticizer / A Fork in The Road / Tunnels Of Light / Dyson Swarm Modules⚠ … 他40件

### Tier 12 - UMV時代  _(L4615)_ — 未翻訳率: 44/45 (98%)

- [ ] L4619-L4793 (44) T4: Advanced / Finally, Universium! / Wireless Multi-Amp Hatches / Magnetohydrodynamically Constrained Star Matter / Guzzling Massive Amounts of Gas / UMV Energy Hatch … 他38件

### エンドゲーム - ゴール  _(L4796)_ — 未翻訳率: 29/30 (97%)

- [ ] L4800-L4914 (29) A Universe In Your Drives⚠ / MAX Circuits / Strings Upon Strings Upon Strings Upon-⚠ / Tier 13 (UXV) / The Door to Heaven? / Stargate Ring Block … 他23件

### 自給自足  _(L4917)_ — 未翻訳率: 8/48 (17%)

- [ ] L5029-L5031 (1) Dezil's Marshmallow
- [ ] L5053-L5067 (4) Really OP Food / Uncooked Slush / Glowing Marshmallow / Cooling Your Marshmallow
- [ ] L5101-L5116 (3) A Magical Lunchbox? / Ice Ice Baby⚠ / The Green Revolution

### 緑の革命  _(L5114)_ — 未翻訳率: 1/162 (1%)

- [ ] L5370-L5372 (1) Platina

### 旅に出かけよう...  _(L5767)_ — 未翻訳率: 24/65 (37%)

- [ ] L5771-L5773 (1) Indestructible Vessel
- [ ] L5779-L5781 (1) Relocator
- [ ] L5815-L5817 (1) Advanced Electric Jetpack
- [ ] L5911-L5913 (1) Travelocity!
- [ ] L5919-L5929 (3) Angel Wings / Secret-Angel-Assasin / Angel Wings - Ultra Force!
- [ ] L5947-L5981 (9) Better Boots with a little pizzazz / Walk all over you / Walking across the stars / Flying Like....Mary Poppins? / Flying With the Greatest of Ease / Working While Flying? … 他3件
- [ ] L5987-L6013 (7) Travelocity² / Let's Go Lava Surfing! / Enhanced Charm of Dislocation / Charm of Dislocation / Planar Gateways / Chaos Locator … 他1件
- [ ] L6023-L6025 (1) Spare Battery

### ...死ぬことなしに  _(L6028)_ — 未翻訳率: 28/99 (28%)

- [ ] L6036-L6046 (3) Protect Your Base: Tier 4 / Make Love, Not War / Why Grenades...
- [ ] L6056-L6070 (4) Protect Your Base: Tier 5 / Turret Base Tier 5 / PewPew! / Railguns, What Else
- [ ] L6096-L6098 (1) Luke, I'm Your Father
- [ ] L6104-L6118 (4) Protect Your Base: Tier 2 / Tier 2 Turret Base / Sometimes, a Bullet Will Do / Burn Them. Burn Them All!
- [ ] L6124-L6142 (5) Protect Your Base: Tier 3 / Tier 3 Base / This is Relatively Useful / Fire in the Hole / Turret Base Tier 4
- [ ] L6208-L6214 (2) Dark Steel Armor Basic Upgrades / Dark Steel Armor Advanced Upgrades
- [ ] L6272-L6294 (6) Nano Goggles / Quantum Goggles / Goggles > 9000 / Compressed Steel Armor / Compressed Desh Armor / Compressed Titanium Armor⚠
- [ ] L6384-L6386 (1) Eldritch Striders⚠
- [ ] L6392-L6394 (1) Apprentice Striders⚠
- [ ] L6404-L6406 (1) Archmage Striders

### キッチリ基地を建築  _(L6425)_ — 未翻訳率: 32/83 (39%)

- [ ] L6429-L6431 (1) Let it Glow!
- [ ] L6437-L6443 (2) Barrel Upgrades⚠ / Texturing made easy
- [ ] L6601-L6607 (2) Lighting Up a Large Area, Without Electricity / Lighting Up a Large Area, With Electricity
- [ ] L6613-L6615 (1) BetterIO?
- [ ] L6649-L6675 (7) Excavation Upgrade / Crystal Shulker Box / Let's get Building! / Chests Had Quite the Glow-up!⚠ / Obsidian Barrel / Obsidian Shulker Box … 他1件
- [ ] L6681-L6683 (1) Iron Shulker Box
- [ ] L6689-L6727 (10) Gotta Go Fast! / Gold Shulker Box / Finally, Some Real Power! / Shulker Upgrades / Diamond Shulker Box / Advanced Concrete Backfiller … 他4件
- [ ] L6733-L6763 (8) Cooper's Mallet / Advanced Filing Cabinet / Marking Your Base⚠ / Silver Shulker Box / Draconic Chest / Concrete Backfiller … 他2件

### Forestryとマルチファーム  _(L6766)_ — 未翻訳率: 22/68 (32%)

- [ ] L6770-L6774 (1) THE RAINMAKER
- [ ] L6792-L6808 (3) The Multifarm / Farm Logic / Changing Your Foresty Circuit Configuration
- [ ] L6818-L6858 (7) Multifarm: Hatch / Multifarm: Valve / Multifarm: Control / Multifarm: Gearbox / Enhanced Farm Logic / Refined Farm Logic … 他1件
- [ ] L6876-L6898 (4) Copper, Tin, Bronze Tubes / Iron, Golden, Diamantine Tubes / Rubberised, Obsidian, Lapis Tubes / Blazing, Ender, Emerald Tubes
- [ ] L6912-L6934 (4) Another Path to Ethanol / Why No, This is Not Fit For Human Consumption / Better Fermenter Outputs / Such Pretty Leaves...
- [ ] L6940-L6944 (1) Seeing the Fruits of Your Labor
- [ ] L6958-L6960 (1) Speak For the Trees
- [ ] L7010-L7014 (1) U-238 Tu-Wait, Seriously?

### マルチブロックの旅  _(L7081)_ — 未翻訳率: 65/118 (55%)

- [ ] L7085-L7091 (2) Distill the Atmosphere / Collision Course
- [ ] L7153-L7163 (3) An Industrial Mobfarm / Powderbarrels / TNT
- [ ] L7205-L7207 (1) Let's Get Crackin!
- [ ] L7229-L7247 (5) Still Not Enough Charcoal? / It's Time to Get More Steam / Steam is Never Enough / Moooooore Steam / Even More Steam? Are You Sure?
- [ ] L7253-L7259 (2) A Very Useful Scanner / The 'Water Problems' Are Solved
- [ ] L7265-L7283 (5) Assembly Line / Data Access Hatches / Time to Drill For Ore! / Thermal Boiler - Lava you long time / Electrum Flux Coil Upgrade
- [ ] L7293-L7295 (1) Helium is Not Just for Balloons
- [ ] L7301-L7347 (12) Playing With the Big Boys, Chemically / Better Glass Upgrade, EV Glass / IV Glass / LuV Glass / ZPM Glass / UV Glass … 他6件
- [ ] L7357-L7363 (2) Getting Muddy With Monazite / Dissolution Tank
- [ ] L7377-L7387 (3) Neutron Activator / Neutron Sensor / Neutron Accelerator
- [ ] L7405-L7427 (6) Focusing Science and Mystery / Catalyzing Miracles / Tier 2 Shielding / Tier 3 Shielding / Tier 4 Shielding / Too much Indium?
- [ ] L7433-L7467 (9) Eternal Coil Upgrade / Algae Pond / Tier 2 Manipulating / A Beginner's Guide to Particle Physics / Producing Solar Panels in BULK!! / Synchrotron (No Relation to the Catalyst) … 他3件
- [ ] L7473-L7495 (6) Don't ask how this works / Decay Warehouse / Don't Lose That Multiblock Miner! / Using That Algae / A Little More Sigma (Squared)⚠ / No More (IC) Engraving
- [ ] L7505-L7511 (2) Filtered Beamline Output Hatch / Component Assembly Line
- [ ] L7521-L7523 (1) Drones are not Drones!
- [ ] L7533-L7551 (5) Draconic Development / One Fluid Tank to Store it All!! / Tier 4 Manipulating / Tier 3 Manipulating / More Algae Uses

### 大量処理  _(L7554)_ — 未翻訳率: 57/66 (86%)

- [ ] L7562-L7692 (33) Big Beautiful Brewery / This Kinda Burns... / Mass Processing at UV and Beyond!⚠ / Fits The Mold / T2 Maceration Stack / Smelt All The Things Stack-Wise...⚠ … 他27件
- [ ] L7698-L7716 (5) MABS / Another Chemical Multiblock? / Mass Processing in LuV⚠ / Clean Implosions?! / Extraction Point
- [ ] L7722-L7736 (4) Insane Voltage Multiblocks / L.A.T.E.X. Cable Coater⚠ / The Form of the Former Former: Reformed⚠ / See You Lather
- [ ] L7746-L7792 (12) Taking Things Apart / Advanced Assembly Line / Advanced Autoclaving / Megalomania⚠ / ...With The Power of Science! / You've Gotta Keep 'Em Separated … 他6件
- [ ] L7798-L7800 (1) Thermic Heating Device⚠
- [ ] L7806-L7812 (2) Engraving With Style / Extreme Voltage Multiblocks

### 発電方法のハウ・トゥー  _(L7819)_ — 未翻訳率: 120/137 (88%)

- [ ] L7823-L7837 (4) Marie Curium? / XL Turbo Steam Turbine / Calcium Bottlenecking / Portable Clean Energy IV
- [ ] L7859-L7929 (18) Power of the Sun at MV Level / Power of the Sun 1x1 MV / Power of the Sun at HV Level / Power of the Sun 1x1 HV / We Need Big Toys / Power of the Sun at LV Level … 他12件
- [ ] L7935-L7957 (6) What Was That? I Can't Hear You Over the Engine! / Power of the Sun at EV Level / Power of the Sun 1x1 EV / Power of the Sun at IV Level / Power of the Sun 1x1 IV / Do You Hear That Engine Revving?
- [ ] L7967-L7973 (2) Fluid Regulator / Gas Turbine
- [ ] L7987-L8061 (19) Rocket Engine EV / Kinetic Wind Power EV / Kinetic Water Power IV / Kinetic Wind Power IV / Kinetic Water Power LuV / Power of the Sun at LuV Level … 他13件
- [ ] L8075-L8113 (10) You Haven't Learned How to Separate Fluids Yet? Seriously? / Acid Trip / Hallucinogenics Not Included / Portable Clean Energy EV / Portable Clean Energy LuV / Portable Clean Energy ZPM … 他4件
- [ ] L8119-L8225 (27) Radioisotope Thermoelectric Generator / Kinetic Power EV / Kinetic Power IV / Kinetic Power LuV / Kinetic Power ZPM / Kinetic Water Power EV … 他21件
- [ ] L8231-L8365 (34) Large Naquadah Reactor / Nuclear Based Fuel (Th) / Nuclear Based Fuel (U) / Nuclear Based Fuel (Pu) / Naquadah Fuel Refinery / Tier 2 Coil … 他28件

### EUの蓄電と変圧  _(L8368)_ — 未翻訳率: 46/63 (73%)

- [ ] L8372-L8382 (3) IV 16A Hatches / Can we get much higher? / Energized Wireless Dynamo Hatch
- [ ] L8424-L8434 (3) EV Battery Buffer / EV Sunnarium Battery / EV GT++ Batteries
- [ ] L8448-L8454 (2) Low Voltage Power Transformer / MV Battery Buffers
- [ ] L8460-L8566 (27) HV Battery Buffers / HV Battery Hulls / HV Battery / EU packets flowing everywhere... / Who Cares About a Little Cancer... / Lapotronic Energy Storage Unit … 他21件
- [ ] L8572-L8602 (8) Gotta Pump It Up / Let it flow, let it floww ... / Extremely Ultimate and Ultimately Extreme / Wireless Power!? / EV 4A Hatches / Power Goggles … 他2件
- [ ] L8608-L8618 (3) IV 4A Hatches / EV 16A Hatches / At last, the final capacitor!

### 石油のための労働  _(L8621)_ — 未翻訳率: 31/46 (67%)

- [ ] L8625-L8647 (6) Maxed Oil Cracker / Super Fuel At The Top / Breaking the Mold / Ultimate Distillation / Hyperheated Steam / Universal Fuel Power
- [ ] L8665-L8671 (2) The Era of Multis / Generator Power
- [ ] L8713-L8803 (23) Using All the Fractions / Oil Cracker / Boosting the Diesel / Special Rubber from Oil / Distilled Heavy Fuel / Acetone and Ethenone … 他17件

### 大衆("マス")のためのバイオ  _(L8806)_ — 未翻訳率: 34/48 (71%)

- [ ] L8850-L8852 (1) Biological Diesel
- [ ] L8858-L8908 (13) Pyrolyse Oven / Large Steel Boiler / Wood Tar / The Most Powerful Biodiesel / Trees Growing Faster / Sapling Power … 他7件
- [ ] L8914-L8944 (8) Green Nitric Acid / Green Ethenone / Green Cetane-Boosted Diesel / Fermented Biomass / Free For All Fertilizer / Methane Stinks … 他2件
- [ ] L8950-L8996 (12) Upgrading Your Benzene / CBD Into Steam / Mass Distilled Water / Nitric And Sulfuric Acid / Titanium Chemical Plant / Nitrobenzene … 他6件

### 原子核物理学は強力  _(L8999)_ — 未翻訳率: 34/57 (60%)

- [ ] L9007-L9009 (1) Focus on Breeding
- [ ] L9019-L9025 (2) Build the Assembly Line First / Improved Fission
- [ ] L9031-L9037 (2) The Path of Fusion / Building the Reactor
- [ ] L9055-L9081 (7) Focus On Power Generation / Liquid Fluorine Thorium Reactor / First Half of LFTR Breeding / Sparge Tower / Fusion Europium / How Much Power From One Reactor? … 他1件
- [ ] L9123-L9193 (18) Nuclear Fuel Processing / Inputs and Outputs in the LFTR / First Steps in Reprocessing / Second Half of LFTR Breeding / Faster Lutetium Excitement / Exciting Liquid Nuking … 他12件
- [ ] L9211-L9225 (4) Duranium and the Beam Crafter⚠ / Reactors are Expensive! / Establishment of Fusion / A Second Reactor?

### スペース・レース  _(L9228)_ — 未翻訳率: 122/141 (87%)

- [ ] L9236-L9266 (8) Can I Build A Mothership For My Father? / The Legs On The Shuttle Rocket Go Step, Step, Step... / Shuttle Nose Cone / A Reward / H8N4C2O4 (Green) Rocket Fuel / Load and Unload the Rocket … 他2件
- [ ] L9308-L9314 (2) Rocket Launch Pad / Gas 'Er Up
- [ ] L9332-L9346 (4) Oxygen Collector / Oxygen Compressor / Parachute / Advanced Wafers
- [ ] L9352-L9646 (74) 1,1-Dimethylhydrazine / Formaldehyde / Space Station / Are You Prepared? / Moon Arrival / Ceres Dungeon … 他68件
- [ ] L9652-L9734 (21) Coal Tar Distilling / Dense Hydrazine / Monomethylhydrazine / CN3H7O3 (Purple) Rocket Fuel / 2-Ethylanthrahydroquinone / 2-Ethylanthraquinone … 他15件
- [ ] L9740-L9790 (13) Proteus Dungeon / Tier 6 Control Computer / Enceladus Dungeon / Space Pumping / How Do I Charge This Stuff?⚠ / steve@mothership:~$ … 他7件

### 基本的な自動化  _(L9793)_ — 未翻訳率: 15/35 (43%)

- [ ] L9801-L9851 (13) Cart Modules: Coal Power / Automated (un-)Loading / Cart Modules: Farming / Cart Modules: Storage / A Simple Cart / Cart Modules: Wood Cutter … 他7件
- [ ] L9921-L9923 (1) Dealing with H2S
- [ ] L9929-L9931 (1) Reward for Desulfurizing Automation

### SFMとコンピューター  _(L9934)_ — 未翻訳率: 53/54 (98%)

- [ ] L9938-L10148 (53) It's everytime these Transistors / Welcome to OpenComputers! / Your First Microchip / Your First Computer / Arithmetic Logic Circuits / All Your Card Are Belong To Us … 他47件

### パイプでロジスティクス  _(L10151)_ — 未翻訳率: 8/31 (26%)

- [ ] L10191-L10197 (2) Sorting Incoming / More ItemSinks in NEI
- [ ] L10207-L10213 (2) There Is Extra Stuff... / Remote requests
- [ ] L10227-L10229 (1) Time to See The Process
- [ ] L10239-L10241 (1) It's DA BEST
- [ ] L10259-L10261 (1) Modular Upgrades
- [ ] L10267-L10269 (1) I NEED THAT!!!!!!

### Applied Energistics  _(L10276)_ — 未翻訳率: 181/185 (98%)

- [ ] L10280-L10316 (9) 1024k Essentia Component / AE Tier 2 Fluid Storage / Quantum Entangled Singularities / Cribs / Need More Information? / 16384k Fluid Component … 他3件
- [ ] L10322-L10324 (1) 16k Item Storage Cell
- [ ] L10330-L10400 (18) Applied Crafting / Getting Your First Processors / Cables / Basic Terminals / Bundled AE Channels / Quantum Storage … 他12件
- [ ] L10406-L10860 (114) Keeping Your Network Happy / Storing Your ME Data / Speeding Up Growth / Perfecting Crystal Growth / Purifying the Impure / Maximum Security⚠ … 他108件
- [ ] L10866-L11020 (39) Co-Processing x256⚠ / 4096k Essentia Storage Cell / Get Your Priorities Straight / 16384k Essentia Component / Hyper Acceleration! / Advanced Neutronium Tech … 他33件

### 養蜂要領を守って  _(L11023)_ — 未翻訳率: 43/83 (52%)

- [ ] L11027-L11029 (1) The Truth About Serum⚠
- [ ] L11035-L11039 (1) Top-Tier Analyzer
- [ ] L11065-L11189 (21) Mutatron / Genetic Sampler / Diamondware / Genetic Imprinter / Genetic Transposer / Advanced Mutatron … 他15件
- [ ] L11247-L11251 (1) Breeding Bees Into Oblivion⚠
- [ ] L11277-L11281 (1) Fastest Way to Get There
- [ ] L11299-L11327 (5) Genepool / Isolator / Sequencer / Polymeriser / Gene Database
- [ ] L11333-L11343 (2) Registry / Droning On⚠
- [ ] L11357-L11361 (1) Keep Calm and Bee On
- [ ] L11367-L11371 (1) Bee Slurry, the Breakfast of, Well, Weirdos
- [ ] L11381-L11397 (3) A Bag for Butterflies, yawn / Only the Best: Tree Breeding / Only the Worst: Trees Suck!
- [ ] L11403-L11429 (6) IAADDS / Pollen Collection Kit / Living It Larvae⚠ / Fluorescent Dye / Enzyme on The Mind⚠ / Growth Medium

### 交配の方蜂(ほうほう)  _(L11432)_ — 未翻訳率: 58/189 (31%)

- [ ] L11436-L11438 (1) MakeMake
- [ ] L11456-L11458 (1) Iridium
- [ ] L11464-L11466 (1) Neutronium
- [ ] L11476-L11478 (1) Naquadah
- [ ] L11496-L11498 (1) Gassy Bees
- [ ] L11528-L11534 (2) End Dust / Indium
- [ ] L11540-L11542 (1) Dragon Blood
- [ ] L11604-L11618 (4) Batty / Ghastly / Smouldering / Refined
- [ ] L11660-L11662 (1) Sandwich
- [ ] L11720-L11722 (1) Oil
- [ ] L11832-L11834 (1) Zinc
- [ ] L11856-L11858 (1) Titanium
- [ ] L11868-L11870 (1) Uranium
- [ ] L11958-L11964 (2) Spirit / Soul
- [ ] L11978-L11984 (2) Rejuvenating / Empowering
- [ ] L11994-L11996 (1) Thaumium Dust
- [ ] L12006-L12008 (1) Thaumic Shards
- [ ] L12022-L12040 (5) Abandoned / Draconic / Wither / Withering / Spiteful
- [ ] L12058-L12068 (3) D-O-B / Ender Shard / Nether Shard
- [ ] L12074-L12172 (25) Energium / Attuned⚠ / Uranus⚠ / Moon / Salt⚠ / Barnarda⚠ … 他19件
- [ ] L12182-L12188 (2) Oberon / Infinity Catalyst

### Hardcore End(er) Expansion  _(L12191)_ — 未翻訳率: 40/40 (100%)

- [ ] L12195-L12353 (40) Spatial Distortions / Dimensional Chest / Is This the End? No, it's the END Dimension⚠ / Ender Towers / Welcome to the End! / Dragon Essence Altar⚠ … 他34件

### 初歩的な魔導学  _(L12356)_ — 未翻訳率: 41/102 (40%)

- [ ] L12360-L12370 (3) The Choice: Ordo / The Choice: Aqua / The Choice: Aer
- [ ] L12376-L12378 (1) Witchy (Wo)man
- [ ] L12400-L12402 (1) Tome of Knowledge
- [ ] L12454-L12472 (5) The Choice: Ignis / The Choice... / The Choice: Terra / The Choice: Perditio / This is the End...
- [ ] L12498-L12512 (4) Infinite... Lava? / Infinite Water! / Improved Armor: Samurai Style / A New Way to "Farm" Resources
- [ ] L12528-L12534 (2) Gold-Banded Greatwood Scepter / Primal Charm
- [ ] L12552-L12558 (2) Division Sigil / Cursed Earth
- [ ] L12564-L12566 (1) Blub Blub Blub.....
- [ ] L12600-L12602 (1) The Night's Not Dark Anymore
- [ ] L12622-L12624 (1) 3 Plus 4, Carry the 2...
- [ ] L12634-L12636 (1) Boots Are Made For Walking
- [ ] L12642-L12644 (1) Infinite Bats! Wait, What??
- [ ] L12660-L12662 (1) Everything Fuzzy? Try Some Lenses
- [ ] L12668-L12678 (3) Gimme gimme gimme / It's Called the Thaumatorium, OK? / Growing Auram
- [ ] L12686-L12692 (2) The Burden of Knowledge / Comparing at a Distance
- [ ] L12700-L12710 (3) Growing Glowstone the Magical Way / Timewood Tree⚠ / Shadow Metal
- [ ] L12724-L12730 (2) Need More Sugar? / Thaumic Dendrology⚠
- [ ] L12742-L12744 (1) Adding More Functions
- [ ] L12754-L12756 (1) Growing your own Knowledge!
- [ ] L12764-L12782 (5) Alleviating Warp / Counting Items / Magical Plants⚠ / Tube Madness / Infinite Durability

### 発展的な魔導学  _(L12785)_ — 未翻訳率: 76/78 (97%)

- [ ] L12789-L13015 (57) Smoke Your Normal Warp Away / Adept Thaumaturgy / An Awesome Magic Conductor / A Silverwood Wand at Last / Creating a Better Wand / More Energetic Screws to Finish the New Wand … 他51件
- [ ] L13021-L13095 (19) Healing Your Nodes / Disenchanted / Fool's Gold / Gen XXXXXXXXXX... / Purge...Some of Your Warp? / Essentia Transmission … 他13件

### カーミー、ハーミー、...波ァ！  _(L13098)_ — 未翻訳率: 36/37 (97%)

- [ ] L13102-L13244 (36) Lord of the Rings? / The Power of Gods / Shards of Opposite Worlds / Unleashed the Power - Cowl / Unbreakable Cowl / Unleashed the Power - Leggings … 他30件

### 杖の杖星とEMT  _(L13247)_ — 未翻訳率: 38/40 (95%)

- [ ] L13251-L13289 (10) An Appropriate Weapon / Dropped in Asgard, Fallen to Earth / Repaired it! / Super-Mjolnir / Sparking Nitor...? / Rechargeable Scribing Tools … 他4件
- [ ] L13295-L13405 (28) I Don't Want to Set the World on Fire / Diggy Diggy Hole / Bzzap! / Trade Offer / Snowball Fight! / Magical Base Defense … 他22件

### 花の力  _(L13408)_ — 未翻訳率: 26/43 (60%)

- [ ] L13412-L13414 (1) Fountain Of Conjuration
- [ ] L13448-L13474 (7) A Glimpse Into A Watery Future / Botanic Infusion / Terrasteel / Alfheim / Round One... FIGHT! / A Deal With Alfar Industries … 他1件
- [ ] L13508-L13578 (18) Anti-Magnetism / Violence Is Blue / Roses Are Blood-Red / Magic Blue Dust / Better Generating Flowers / Shut Down Your Canning Machine … 他12件

### "端"に目を向ける  _(L13581)_ — 未翻訳率: 91/93 (98%)

- [ ] L13585-L13679 (24) Fire Burn and... / Offerings / ...Cauldron Bubble / Don't Touch the Needle! / Probably Usable For Soup / Don't Shake it Too Much … 他18件
- [ ] L13685-L13951 (67) Purified Milk / Brew of Love / Sleep Well! / The Spirit World - Nightmare / Early Bird Gets the...Nightmare? / Wake Up Early … 他61件

### 高い対価を払って  _(L13954)_ — 未翻訳率: 73/74 (99%)

- [ ] L13958-L14248 (73) Incense Crucible / Tier 2 Sigils / Paying the Highest Price / Portable Battery... / Poke / Tier 3 Sigils … 他67件

### 全部ブッ殺せ  _(L14251)_ — 未翻訳率: 153/344 (44%)

- [ ] L14255-L14289 (9) Time To Kill (Crimson Knight)⚠ / Kill Baba Yaga / Kill Horned Huntsman / Kill Ender Dragon / Kill Shade of Leonard / Kill Lord of Tormentum … 他3件
- [ ] L14299-L14309 (3) Slay the Eyes! / Ender Guardians / Slay the Dragon. (Again)
- [ ] L14451-L14465 (4) Time to Kill (Fire Golem) / Time to kill (Haunted Miners) / Time to Kill (Louse) / Time to Kill (Scorching Lens)
- [ ] L14590-L14612 (6) Something From Nothing Pt 2 / Industrial Water Purification / Waterproof Tech / Integrated Ore Factory - All in One! / Proto-Volt Stabilizer⚠ / Streamlined Casters⚠
- [ ] L14650-L14656 (2) Dark Steel Tools / And It Will Never Break
- [ ] L14666-L14668 (1) Monitoring Your Reactor
- [ ] L14686-L14696 (3) Magical Waystones / Industrial 3D Copying Machine / Draconic Evolution
- [ ] L14742-L14748 (2) Advanced Nano Chestplate / Gravi Suit
- [ ] L14754-L14760 (2) Dark Steel Tool and Weapon Basic Upgrades / Dark Steel Tool and Weapon Advanced Upgrades
- [ ] L14790-L14792 (1) Power of the Sun ULV
- [ ] L14810-L14812 (1) Moron's Guide to Better Trees
- [ ] L14866-L14872 (2) Making Power With Your Plasma / Turbine Time
- [ ] L14906-L14912 (2) Need a Place For All Those Ores? / Angel Wings - Combine!
- [ ] L14918-L14936 (5) Pimp Your Wand Focus / Mallard Rust Smelly / Shake That Booty... / Launch Controller / Arc Lamp
- [ ] L14986-L14988 (1) Planetary Tears
- [ ] L14994-L14996 (1) Don't Put a Finger in That Socket
- [ ] L15014-L15024 (3) Too Much Mercury? / I'll Send Wireless Signals Where I Want, Thank You / Wireless 3.0
- [ ] L15042-L15072 (8) Unlimited LP / Infinity Chest / UV Solar / Does Anyone Even Still Use These? / Transform and...Stay Put Actually / What Even is This? … 他2件
- [ ] L15078-L15080 (1) 「 」
- [ ] L15086-L15128 (11) Nano Forge Tier 2 / Nano Forge Tier 3 / Chemical Pseudo-Altercations / Precise Assembler / Industrial Coke Oven / Bet On The Distillus … 他5件
- [ ] L15134-L15192 (15) Power in the Ether / PCB Factory / Bio Chamber / Liquid Cooling Tower / PCB Factory Tier 2 / Liquid Cooling Tower Tier 2⚠ … 他9件
- [ ] L15198-L15212 (4) Heliocast Reinforcement⚠ / Balance is Everything / Asgardandelion / Celestial Gateways
- [ ] L15218-L15220 (1) Large Molecular Assembler
- [ ] L15226-L15232 (2) Sentient Overclocker⚠ / Large Hadron Collider
- [ ] L15246-L15268 (6) The Quest for Holy Water / High Energy Laser Purification / Neutronium Compressor / Matter Manipulator MKI / Universal Collapser⚠ / Matter Manipulator MKIII
- [ ] L15278-L15292 (4) Absolute Purity / Crafting Input Proxy / The Everlasting Guilty Pool / pH Neutralization
- [ ] L15298-L15300 (1) Hypercooler⚠
- [ ] L15306-L15308 (1) Nano Forge Tier 4
- [ ] L15314-L15320 (2) Never Hungry Again / Quantum Uplink
- [ ] L15326-L15328 (1) Clarifier
- [ ] L15334-L15336 (1) Purifying Water With Plasma
- [ ] L15342-L15344 (1) Flocculation
- [ ] L15350-L15364 (4) Crafting, but with Beams!⚠ / Thaumometric Essentia Cell / Creative Mana Tablet / Exo-Foundry⚠
- [ ] L15369-L15395 (7) Trigger: Nano Boots of the Traveller Skip / Trigger: Runeforged Thaumaturge's Ring / Trigger: Nightvision Goggle Skip / Trigger: Hafnium Skip / Trigger: Rocket Shuttle Skip / Trigger: Naquadria Skip … 他1件
- [ ] L15429-L15431 (1) Bees Template
- [ ] L15457-L15459 (1) Trigger: Flippers
- [ ] L15501-L15567 (17) Tool: Never complete / Trigger: Quantum Armor Skip / Trigger: NaK Skip / Trigger: Dense Hydrazine Skip / Trigger: Zirconium Skip / Trigger: Netherite Skip … 他11件
- [ ] L15573-L15607 (9) Trigger: Rocket Tier 2 Skip / Trigger: SMD Inductor Skip / Trigger: Division Sigil / Trigger: Polyphenylene Sulfide Skip / Trigger: Rocket Tier 7 Skip / Trigger: Profane Wand … 他3件
- [ ] L15613-L15639 (7) Trigger: Prismarine Line Skip / Trigger: CN3H7O3 (Purple) Rocket Fuel Skip / Ice Cream Trophy⚠ / Trigger: Oblivion Frame / Trigger: Rocket Tier 6 Skip / Trigger: Stonelily Tutorial Skip⚠ … 他1件

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
- L3858 Wormhole Generator — v2.9新規(2.8.4に無くゲーム内未確認)
- L4063 Elastic Singularity — v2.9新規(2.8.4に無くゲーム内未確認)
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
- L4566 Energised Tesseract — v2.9新規(2.8.4に無くゲーム内未確認)
- L4610 Maybe I Do Need These — v2.9新規(2.8.4に無くゲーム内未確認)
- L4643 Zepto Power IC — v2.9新規(2.8.4に無くゲーム内未確認)
- L4675 Resplendent Components — v2.9新規(2.8.4に無くゲーム内未確認)
- L4691 Reinforced Components — v2.9新規(2.8.4に無くゲーム内未確認)
- L4699 Perfected Components — v2.9新規(2.8.4に無くゲーム内未確認)
- L4707 T7: Perfect — v2.9新規(2.8.4に無くゲーム内未確認)
- L4715 A Solder Singularity — v2.9新規(2.8.4に無くゲーム内未確認)
- L4719 T2: Primitive — v2.9新規(2.8.4に無くゲーム内未確認)
- L4755 T8: Tipler — v2.9新規(2.8.4に無くゲーム内未確認)
- L4771 Refined Components — v2.9新規(2.8.4に無くゲーム内未確認)
- L4787 T5: Superb — v2.9新規(2.8.4に無くゲーム内未確認)
- L4800 A Universe In Your Drives — v2.9新規(2.8.4に無くゲーム内未確認)
- L4808 Strings Upon Strings Upon Strings Upon- — v2.9新規(2.8.4に無くゲーム内未確認)
- L4836 You'll Only Need a Few of These — ID使い回し(2.8.4「You'll Probably Need Quite a Few of These」→2.9「§6§l§nYou'll Only Need a Few of These」ゲーム内未確認)
- L4852 UXV Energy Hatch — v2.9新規(2.8.4に無くゲーム内未確認)
- L4900 A Minor Roadblock — v2.9新規(2.8.4に無くゲーム内未確認)
- L5105 Ice Ice Baby — v2.9新規(2.8.4に無くゲーム内未確認)
- L6292 Compressed Titanium Armor — ID使い回し(2.8.4「Compressed Titan Armor」→2.9「Compressed Titanium Armor」ゲーム内未確認)
- L6384 Eldritch Striders — v2.9新規(2.8.4に無くゲーム内未確認)
- L6392 Apprentice Striders — v2.9新規(2.8.4に無くゲーム内未確認)
- L6437 Barrel Upgrades — v2.9新規(2.8.4に無くゲーム内未確認)
- L6661 Chests Had Quite the Glow-up! — v2.9新規(2.8.4に無くゲーム内未確認)
- L6741 Marking Your Base — v2.9新規(2.8.4に無くゲーム内未確認)
- L7461 Stern-Gerlach, Perhaps? — v2.9新規(2.8.4に無くゲーム内未確認)
- L7489 A Little More Sigma (Squared) — v2.9新規(2.8.4に無くゲーム内未確認)
- L7570 Mass Processing at UV and Beyond! — v2.9新規(2.8.4に無くゲーム内未確認)
- L7582 Smelt All The Things Stack-Wise... — ID使い回し(2.8.4「Smelt All the Things Stack-Wise...」→2.9「§5§lSmelt All The Things Stack-Wise...」ゲーム内未確認)
- L7590 A Volcano For Your Base. — ID使い回し(2.8.4「A volcano for your base.」→2.9「§9§lA Volcano For Your Base.」ゲーム内未確認)
- L7606 The Rocks In The Washer... — ID使い回し(2.8.4「The rocks in the washer...」→2.9「§8§lThe Rocks In The Washer...」ゲーム内未確認)
- L7610 Dancing In Circles — ID使い回し(2.8.4「Dancing in circles」→2.9「§8§lDancing In Circles」ゲーム内未確認)
- L7614 I Think I'm Going to be Sick — ID使い回し(2.8.4「I think I'm going to be sick」→2.9「§8§lI Think I'm Going to be Sick」ゲーム内未確認)
- L7618 Bask In The Currents — ID使い回し(2.8.4「Bask in the currents」→2.9「§9§lBask In The Currents」ゲーム内未確認)
- L7626 Play-Doh For Big Girls and Boys — ID使い回し(2.8.4「Play doh for big girls and boys」→2.9「§9§lPlay-Doh For Big Girls and Boys」ゲーム内未確認)
- L7630 Best Thing Since Sliced Bread — ID使い回し(2.8.4「Best thing since sliced bread」→2.9「§9§lBest Thing Since Sliced Bread」ゲーム内未確認)
- L7646 Spools and Spools — ID使い回し(2.8.4「Spools and spools」→2.9「§9§lSpools and Spools」ゲーム内未確認)
- L7650 Bender, More Bending! — ID使い回し(2.8.4「Bender more bending」→2.9「§8§lBender, More Bending!」ゲーム内未確認)
- L7654 Bezos Would Be Proud — ID使い回し(2.8.4「Bezos would be proud」→2.9「§9§lBezos Would Be Proud」ゲーム内未確認)
- L7666 Empty The Oceans — ID使い回し(2.8.4「Empty the oceans」→2.9「§9§lEmpty The Oceans」ゲーム内未確認)
- L7670 Putting All Those Workers Out of Jobs — ID使い回し(2.8.4「Putting all those workers out of jobs」→2.9「§b§lPutting All Those Workers Out of Jobs」ゲーム内未確認)
- L7682 Cool Guys Don't Look At Explosions — ID使い回し(2.8.4「Cool Guys Don't Look at Explosions」→2.9「§9§lCool Guys Don't Look At Explosions」ゲーム内未確認)
- L7686 Let Me Fabricate a New Universe... — ID使い回し(2.8.4「Let me fabricate a new universe...」→2.9「§b§lLet Me Fabricate a New Universe...」ゲーム内未確認)
- L7690 I Want SOLIDS Not LIQUIDS! — ID使い回し(2.8.4「I Want SOLIDS not LIQUIDS!」→2.9「§9§lI Want SOLIDS Not LIQUIDS!」ゲーム内未確認)
- L7706 Mass Processing in LuV — ID使い回し(2.8.4「Mass Processing in LuV and Beyond」→2.9「§d§lMass Processing in LuV」ゲーム内未確認)
- L7726 L.A.T.E.X. Cable Coater — v2.9新規(2.8.4に無くゲーム内未確認)
- L7730 The Form of the Former Former: Reformed — v2.9新規(2.8.4に無くゲーム内未確認)
- L7758 Megalomania — v2.9新規(2.8.4に無くゲーム内未確認)
- L7778 Can It! — ID使い回し(2.8.4「Can it!」→2.9「§5§lCan It!」ゲーム内未確認)
- L7782 Spinmatron-2737 — v2.9新規(2.8.4に無くゲーム内未確認)
- L7798 Thermic Heating Device — v2.9新規(2.8.4に無くゲーム内未確認)
- L8793 Higher Capacity Dynamo — ID使い回し(2.8.4「Buffered Dynamo」→2.9「Higher Capacity Dynamo」ゲーム内未確認)
- L9211 Duranium and the Beam Crafter — ID使い回し(2.8.4「Duranium and the Cyclotron」→2.9「Duranium and the Beam Crafter」ゲーム内未確認)
- L9756 How Do I Charge This Stuff? — ID使い回し(2.8.4「How the Eff Do I Charge This Sh*t?」→2.9「How Do I Charge This Stuff?」ゲーム内未確認)
- L10306 Pattern Repeater — v2.9新規(2.8.4に無くゲーム内未確認)
- L10426 Maximum Security — ID使い回し(2.8.4「Wireless Setup」→2.9「Maximum Security」ゲーム内未確認)
- L10578 Easier AL Automation — ID使い回し(2.8.4「Easier AL automation」→2.9「Easier AL Automation」ゲーム内未確認)
- L10866 Co-Processing x256 — v2.9新規(2.8.4に無くゲーム内未確認)
- L10918 Co-Processing x1024 — v2.9新規(2.8.4に無くゲーム内未確認)
- L10942 Advanced Level Emitter — v2.9新規(2.8.4に無くゲーム内未確認)
- L10962 Co-Processing x64 — v2.9新規(2.8.4に無くゲーム内未確認)
- L10970 Certified Geek, 7 Days a Week — v2.9新規(2.8.4に無くゲーム内未確認)
- L11006 Co-Processing x4096 — v2.9新規(2.8.4に無くゲーム内未確認)
- L11027 The Truth About Serum — v2.9新規(2.8.4に無くゲーム内未確認)
- L11247 Breeding Bees Into Oblivion — ID使い回し(2.8.4「Bees Buzzing Beyond the Dark」→2.9「Breeding Bees Into Oblivion」ゲーム内未確認)
- L11339 Droning On — ID使い回し(2.8.4「Inoculator」→2.9「Droning On」ゲーム内未確認)
- L11415 Living It Larvae — v2.9新規(2.8.4に無くゲーム内未確認)
- L11423 Enzyme on The Mind — v2.9新規(2.8.4に無くゲーム内未確認)
- L12078 Attuned — v2.9新規(2.8.4に無くゲーム内未確認)
- L12082 Uranus — v2.9新規(2.8.4に無くゲーム内未確認)
- L12090 Salt — v2.9新規(2.8.4に無くゲーム内未確認)
- L12094 Barnarda — v2.9新規(2.8.4に無くゲーム内未確認)
- L12102 Infinity — v2.9新規(2.8.4に無くゲーム内未確認)
- L12106 Infernal — v2.9新規(2.8.4に無くゲーム内未確認)
- L12110 Trinium — v2.9新規(2.8.4に無くゲーム内未確認)
- L12126 Oriharukon — v2.9新規(2.8.4に無くゲーム内未確認)
- L12134 Enceladus — v2.9新規(2.8.4に無くゲーム内未確認)
- L12138 Saturn — v2.9新規(2.8.4に無くゲーム内未確認)
- L12142 Barnarda F — v2.9新規(2.8.4に無くゲーム内未確認)
- L12150 Pluto — v2.9新規(2.8.4に無くゲーム内未確認)
- L12154 Neptune — v2.9新規(2.8.4に無くゲーム内未確認)
- L12162 Mars — v2.9新規(2.8.4に無くゲーム内未確認)
- L12170 Jupiter — v2.9新規(2.8.4に無くゲーム内未確認)
- L12203 Is This the End? No, it's the END Dimension — ID使い回し(2.8.4「Is This the End? No it's the END Dimension」→2.9「Is This the End? No, it's the END Dimension」ゲーム内未確認)
- L12215 Dragon Essence Altar — ID使い回し(2.8.4「Essence Altar Dragon Infused」→2.9「Dragon Essence Altar」ゲーム内未確認)
- L12235 Visit the (Enchanted) Laboratory Island — ID使い回し(2.8.4「Visit the Laboratory Island」→2.9「Visit the (Enchanted) Laboratory Island」ゲーム内未確認)
- L12239 Energy Clusters and the Energy Wand — ID使い回し(2.8.4「Energy Wand」→2.9「Energy Clusters and the Energy Wand」ゲーム内未確認)
- L12243 Visit the (Enchanted) Homeland Island — ID使い回し(2.8.4「Visit the Enchanted Island」→2.9「Visit the (Enchanted) Homeland Island」ゲーム内未確認)
- L12704 Timewood Tree — v2.9新規(2.8.4に無くゲーム内未確認)
- L12728 Thaumic Dendrology — v2.9新規(2.8.4に無くゲーム内未確認)
- L12772 Magical Plants — v2.9新規(2.8.4に無くゲーム内未確認)
- L13061 Primordial Armor — v2.9新規(2.8.4に無くゲーム内未確認)
- L13069 Infused Seeds — v2.9新規(2.8.4に無くゲーム内未確認)
- L13230 Runeforged Thaumaturge's Ring — v2.9新規(2.8.4に無くゲーム内未確認)
- L13234 Master Earth Rings — v2.9新規(2.8.4に無くゲーム内未確認)
- L13238 Ring of the Sky — v2.9新規(2.8.4に無くゲーム内未確認)
- L14238 Ritual of Gaia's Transformation — v2.9新規(2.8.4に無くゲーム内未確認)
- L14255 Time To Kill (Crimson Knight) — ID使い回し(2.8.4「Secrets」→2.9「Time To Kill (Crimson Knight)」ゲーム内未確認)
- L14606 Proto-Volt Stabilizer — v2.9新規(2.8.4に無くゲーム内未確認)
- L14610 Streamlined Casters — v2.9新規(2.8.4に無くゲーム内未確認)
- L15110 Faster Basic Crops — ID使い回し(2.8.4「§6§lFaster Crops」→2.9「§6§lFaster Basic Crops」ゲーム内未確認)
- L15118 High Temperature Gas-cooled Reactor — ID使い回し(2.8.4「§6§lHigh Temperature Super Breeder」→2.9「§6§lHigh Temperature Gas-cooled Reactor」ゲーム内未確認)
- L15154 Liquid Cooling Tower Tier 2 — ID使い回し(2.8.4「Thermosink Radiator」→2.9「§c§l§nLiquid Cooling Tower Tier 2」ゲーム内未確認)
- L15186 Superdense Casting Basins — v2.9新規(2.8.4に無くゲーム内未確認)
- L15198 Heliocast Reinforcement — v2.9新規(2.8.4に無くゲーム内未確認)
- L15226 Sentient Overclocker — v2.9新規(2.8.4に無くゲーム内未確認)
- L15262 Universal Collapser — v2.9新規(2.8.4に無くゲーム内未確認)
- L15298 Hypercooler — v2.9新規(2.8.4に無くゲーム内未確認)
- L15350 Crafting, but with Beams! — v2.9新規(2.8.4に無くゲーム内未確認)
- L15362 Exo-Foundry — v2.9新規(2.8.4に無くゲーム内未確認)
- L15561 Trigger: Air-Filter — v2.9新規(2.8.4に無くゲーム内未確認)
- L15621 Ice Cream Trophy — v2.9新規(2.8.4に無くゲーム内未確認)
- L15633 Trigger: Stonelily Tutorial Skip — v2.9新規(2.8.4に無くゲーム内未確認)


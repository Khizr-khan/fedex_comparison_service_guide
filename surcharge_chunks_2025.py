"""
surcharge_chunks_2025.py — FedEx 2025 surcharge strings.

Extracted directly from FedEx 2025 Service Guide PDF pages 128-144.
Effective January 6, 2025 (updated September 22, 2025).

KEY DIFFERENCES FROM 2026:
- Additional Handling (dimension): Zone 2 $28 (vs $29.50), Zones 3-4 $31 (vs $32.75),
  Zones 5-6 $36 (vs $38.50), Zones 7+ $38 (vs $40.75)
- Additional Handling (weight): Zone 2 $43.50 (vs $46), Zones 3-4 $47.50 (vs $50.25),
  Zones 5-6 $52.75 (vs $56.25), Zones 7+ $55 (vs $58.75)
- Additional Handling (packaging): Zone 2 $25 (vs N/A separate), Zones 3-4 $29, Zones 5-6 $31, Zones 7+ $31.50
- Additional Handling (intl): $27 dimension, $38 weight, $27 packaging (vs $26.50/$30.75/$33.75)
- Oversize (intl): $190 (vs $208)
- Oversize (U.S.): Zone 2 $240, Zones 3-4 $260, Zones 5-6 $297.50, Zones 7+ $305 (vs $255/$275/$320/$330)
- Unauthorized (intl): $660 (vs $700), Intl Express Freight $1,325 (vs $1,400), U.S. Ground $1,775 (vs $1,875)
- Address Correction (packages): $24 (vs $25.50)
- Payer Rebilling: $24 (vs $25.50)
- Reroute (packages): $24 (vs $25.50)
- Missing Account Number: $24 (vs $25.50)
- Residential Delivery (U.S. Express): $6.55 (vs $6.95), Ground/Home Delivery $5.95 (vs $6.45)
- Residential freight: $215 (vs $230)
- Signature (Indirect/Direct): $7.15 (vs $7.60), Adult: $8.65 (vs $10.00)
- Signature multiweight max: $50.05 Indirect/Direct, $60.55 Adult (vs $53.20/$70)
- Home Delivery Date Certain: $4.65 (vs $4.95), Evening: $10.50 (vs $11.25), Appointment: $24 (vs $25.50)
- DAS Commercial: $4.20 (vs $4.45), Extended Commercial: $5.25 (vs $8.80),
  Residential: $6.20 (vs $6.60), Extended Residential: $8.30 (vs $8.80), Remote: $15.50 (vs $22.25+)
- Delivery Reattempt: $91.50 or $0.100/lb (vs $97 or $0.106/lb)
- Dangerous Goods (Intl accessible): $240 or $1.40/lb (vs $240 or $1.48/lb)
- Dangerous Goods (Intl inaccessible): $115 or $0.67/lb (vs $115 or $0.71/lb)
- Dangerous Goods (Intl Express Freight accessible): $255 or $1.40/lb (vs $270 or $1.48/lb)
- Dangerous Goods (Intl Express Freight inaccessible): $145 or $0.67/lb (vs $153.50 or $0.71/lb)
- Dangerous Goods (FO/1Day Freight accessible): $175 or $1.40/lb (vs $185 or $1.48/lb)
- Dangerous Goods (2Day/3Day Freight inaccessible): $145 or $0.50/lb (vs $153.50 or $0.53/lb)
- Declared Value: $4.50 for $100.01-$300, then $1.50/$100 over $300 (vs flat $1.65/$100 over $100)
- Northern Canada: $105 (<=70 lbs) (vs $110), $165 (>70 lbs) (vs $175)
- Out-of-Delivery-Area Tier A: $4.20 (vs $4.45), Tier B: $49 or $0.49/lb (vs same), Tier C: $64 or $0.64/lb (vs $68 or $0.68/lb)
- Out-of-Delivery-Area Freight: Tier B $245 (vs $260), Tier C $320 (vs $340)
- Metro Service Area: $245 (vs $260)
- Extended Service Area (Freight): $245 (vs $260)
- Hazmat Ground: $54 (vs $57.25)
- Inside Delivery/Pickup: $150.50 or $0.099/lb (vs $160 or $0.105/lb)
- Priority Alert (Intl First/Priority): $28.50 or $0.57/lb (vs $30.05 or $0.60/lb)
- Priority Alert (Intl Priority Freight): $230 or $0.23/lb (vs $240 or $0.24/lb)
- Priority Alert Plus (Intl First/Priority): $34 or $0.68/lb (vs $36 or $0.72/lb)
- Priority Alert Plus (Intl Priority Freight): $290 or $0.29/lb (vs $310 or $0.31/lb)
- Priority Alert Plus (U.S. Express Freight): $199 or $0.34/lb (vs $210.75 or $0.36/lb)
- U.S. Inbound Processing: $2.50 (vs $2.65)
- Return Manager/Call Tag (Ground commercial): $8.30 (vs $8.80), Residential: $9.50 (vs $10.00)
- EEI Filing: $13 (same)
- Broker In-Bond Transfer: $90 (same)
- SenseAware: same as 2026
- Clearance Canada: same tiers as 2026
- Canada-to-U.S. Clearance: $800.01-$1,250 = $28.75 (vs $30.50), $1,250.01-$2,000 = $40.50 (vs $42.25),
  over $2,000 = $40.50 + $1.95/additional $1,000 (vs $42.25 + $1.95)
"""

SURCHARGE_CHUNKS = [
    # ── Additional Handling (U.S. Package — Dimension) ────────────────────────
    "Additional Handling surcharge for dimension: Zone 2 rate is $28.00.",
    "Additional Handling surcharge for dimension: Zones 3-4 rate is $31.00.",
    "Additional Handling surcharge for dimension: Zones 5-6 rate is $36.00.",
    "Additional Handling surcharge for dimension: Zones 7 and above rate is $38.00.",

    # ── Additional Handling (U.S. Package — Weight) ───────────────────────────
    "Additional Handling surcharge for weight or packaging over 50 lbs: Zone 2 rate is $43.50.",
    "Additional Handling surcharge for weight or packaging over 50 lbs: Zones 3-4 rate is $47.50.",
    "Additional Handling surcharge for weight or packaging over 50 lbs: Zones 5-6 rate is $52.75.",
    "Additional Handling surcharge for weight or packaging over 50 lbs: Zones 7 and above rate is $55.00.",

    # ── Additional Handling (U.S. Package — Packaging/non-standard) ──────────
    "Additional Handling surcharge for non-standard packaging: Zone 2 rate is $25.00.",
    "Additional Handling surcharge for non-standard packaging: Zones 3-4 rate is $29.00.",
    "Additional Handling surcharge for non-standard packaging: Zones 5-6 rate is $31.00.",
    "Additional Handling surcharge for non-standard packaging: Zones 7 and above rate is $31.50.",

    # ── Additional Handling (International Package) ───────────────────────────
    "Additional Handling surcharge for international dimension is $27.00 per package.",
    "Additional Handling surcharge for international weight is $38.00 per package.",
    "Additional Handling surcharge for international packaging is $27.00 per package.",

    # ── Additional Handling (Express Freight) ─────────────────────────────────
    "Additional Handling surcharge for U.S. Express Freight is $270.00 per freight handling unit.",
    "Additional Handling surcharge for International Priority Freight, International Economy Freight, or International Deferred Freight is $260.00 per freight handling unit.",
    "Additional Handling Non-stackable surcharge for U.S. Express Freight is $340.00 per freight handling unit.",
    "Additional Handling Non-stackable surcharge for International Express Freight is $330.00 per freight handling unit.",

    # AHS alias
    "AHS (Additional Handling Surcharge) for dimension Zone 2 is $28.00.",
    "AHS (Additional Handling Surcharge) for dimension Zones 3-4 is $31.00.",
    "AHS (Additional Handling Surcharge) for dimension Zones 5-6 is $36.00.",
    "AHS (Additional Handling Surcharge) for dimension Zones 7+ is $38.00.",

    # ── Oversize ──────────────────────────────────────────────────────────────
    "Oversize charge for U.S. Package: Zone 2 rate is $240.00.",
    "Oversize charge for U.S. Package: Zones 3-4 rate is $260.00.",
    "Oversize charge for U.S. Package: Zones 5-6 rate is $297.50.",
    "Oversize charge for U.S. Package: Zones 7 and above rate is $305.00.",
    "Oversize charge for Home Delivery: Zone 2 rate is $240.00.",
    "Oversize charge for Home Delivery: Zones 3-4 rate is $260.00.",
    "Oversize charge for Home Delivery: Zones 5-6 rate is $297.50.",
    "Oversize charge for Home Delivery: Zones 7 and above rate is $305.00.",
    "Oversize charge for International packages is $190.00.",

    # ── Unauthorized Package ──────────────────────────────────────────────────
    "Unauthorized Package surcharge for International packages is $660.00.",
    "Unauthorized Package surcharge for International Express Freight is $1,325.00.",
    "Ground Unauthorized Package surcharge for FedEx Ground, Home Delivery, or International Ground is $1,775.00.",

    # ── Pickup — Automated ────────────────────────────────────────────────────
    "Automated Pickup fee is $19.00 per week.",
    "Pickup Automated weekly fee is $19.00.",

    # ── Pickup — Future Day On-Call ───────────────────────────────────────────
    "Pickup Future Day on-call via online: Monday through Friday is $9.00.",
    "Pickup Future Day on-call via online: Saturday is $15.50.",
    "Pickup Future Day on-call via phone: Monday through Friday is $10.50.",
    "Pickup Future Day on-call via phone: Saturday is $17.00.",

    # ── Pickup — Same Day On-Call ─────────────────────────────────────────────
    "Pickup Same Day on-call via online: Monday through Friday is $14.75.",
    "Pickup Same Day on-call via online: Saturday is $21.25.",
    "Pickup Same Day on-call via phone: Monday through Friday is $16.25.",
    "Pickup Same Day on-call via phone: Saturday is $22.75.",

    # ── Pickup — Regularly Scheduled ─────────────────────────────────────────
    "Pickup Regularly Scheduled 1 day per week is $7.50 per week.",
    "Pickup Regularly Scheduled 2 days per week is $15.00 per week.",
    "Pickup Regularly Scheduled 3 days per week is $22.00 per week.",
    "Pickup Regularly Scheduled 4 days per week is $29.00 per week.",
    "Pickup Regularly Scheduled 5 days per week is $35.50 per week.",
    "Weekly Pickup Regularly Scheduled 5 days is $35.50.",

    # ── Pickup — Saturday/Sunday ──────────────────────────────────────────────
    "Pickup Saturday or Sunday Regularly Scheduled is $12.00 per day.",
    "Saturday Automated Pickup fee is $7.95 per day.",

    # ── Pickup Area Surcharges ────────────────────────────────────────────────
    "Pickup Area surcharge Residential is $5.95.",
    "Pickup Area surcharge Pickup Area is $6.20.",
    "Pickup Area surcharge Extended Area is $8.30.",
    "Pickup Area surcharge Remote is $15.50.",

    # ── Address Correction ────────────────────────────────────────────────────
    "Address Correction surcharge for packages is $24.00.",
    "Address Correction surcharge for freight is $130.00.",
    "Address Correction Multiweight Ground maximum per shipment is $72.00.",
    "Address Correction Multiweight Express maximum per shipment is $168.00.",
    "Wrong address correction fee is $24.00 per package.",
    "Incorrect address fee is $24.00.",
    "Bad address correction surcharge is $24.00.",

    # ── Broker Fees ───────────────────────────────────────────────────────────
    "Broker Document Transfer fee is $51.00.",
    "Broker In-Bond Transfer fee is $90.00.",

    # ── Clearance — U.S. Import ───────────────────────────────────────────────
    "Clearance U.S. Import Entry Copy fee is $2.10.",
    "Clearance U.S. Import Entry of Goods (Government Entries) fee is $53.00.",
    "Clearance U.S. Import Live Entry Processing fee is $27.00.",
    "Clearance U.S. Import Prior Notice for Food and Food Products fee is $13.50.",
    "Clearance U.S. Import storage fee is $0.08 per kg per business day plus $20.00 base starting from the 3rd day.",
    "Clearance U.S. Import Disbursement Fee: if customs value is $800 or less, the fee is the greater of $4.50 or 2% of Duty and Tax. If customs value exceeds $800, the fee is the greater of $14 or 2% of Duty and Tax.",
    "Clearance U.S. Import Duty and Tax Forwarding Fee: if customs value is $800 or less, the fee is the greater of $8.50 or 2% of Duty and Tax. If customs value exceeds $800, the fee is the greater of $27 or 2% of Duty and Tax.",
    "Clearance U.S. Import Duty and Tax Forwarding Fee: if customs value is $800 or less, the fee is the greater of $8.50 or 2% of Duty and Tax. If customs value exceeds $800, the fee is the greater of $27 or 2% of Duty and Tax.",

    # ── Clearance — Temporary Import ─────────────────────────────────────────
    "Clearance Temporary Import Entry fee is $150.00.",

    # ── Clearance — Government Agencies ──────────────────────────────────────
    "Clearance ATF (Bureau of Alcohol, Tobacco, Firearms and Explosives) fee is $74.00.",
    "Clearance FWS (Fish and Wildlife Service) fee is the actual FWS fees plus an additional $22.00 FedEx administrative fee.",
    "Clearance FDA (Food and Drug Administration) fee is $27.50.",
    "Clearance Additional Entry Line Items fee is $3.50 per line over 3 lines.",

    # ── Clearance — Canada (U.S. to Canada) ──────────────────────────────────
    "Clearance Canada U.S.-to-Canada shipment value $0 to $40.00: fee is $0.",
    "Clearance Canada U.S.-to-Canada shipment value $40.01 to $60.00: fee is $17.25.",
    "Clearance Canada U.S.-to-Canada shipment value $60.01 to $100.00: fee is $21.25.",
    "Clearance Canada U.S.-to-Canada shipment value $100.01 to $150.00: fee is $27.50.",
    "Clearance Canada U.S.-to-Canada shipment value $150.01 to $200.00: fee is $32.25.",
    "Clearance Canada U.S.-to-Canada shipment value $200.01 to $500.00: fee is $54.00.",
    "Clearance Canada U.S.-to-Canada shipment value $500.01 to $1000.00: fee is $62.00.",
    "Clearance Canada U.S.-to-Canada shipment value $1000.01 to $1600.00: fee is $71.50.",
    "Clearance Canada U.S.-to-Canada shipment value $1600.01 to $3300.00: fee is $82.00.",
    "Clearance Canada U.S.-to-Canada shipment value over $3300.00: fee is $82.00 plus $7.50 per additional $1000.",
    "Clearance Canada additional line fee is CAD$5.30 per extra line.",
    "Clearance Canada disbursement fee is the greater of CAD$11.40 or 2.95% of duty-and-tax charges.",
    "Clearance Canada Temporary Import Entry fee is CAD$120.00.",
    "Clearance Canada OGA (Other Government Agency) fee is CAD$16.50.",
    "Clearance Canada Fax fee is CAD$3.00.",
    "Clearance Canada Call fee is CAD$4.00 long distance.",

    # ── Clearance — Canada to U.S. ────────────────────────────────────────────
    "Clearance Canada-to-U.S. shipment value $0 to $200.00: fee is $9.75.",
    "Clearance Canada-to-U.S. shipment value $200.01 to $800.00: fee is $19.50.",
    "Clearance Canada-to-U.S. shipment value $800.01 to $1250.00: fee is $28.75.",
    "Clearance Canada-to-U.S. shipment value $1250.01 to $2000.00: fee is $40.50.",
    "Clearance Canada-to-U.S. shipment value over $2000.00: fee is $40.50 plus $1.95 per additional $1000.",
    "Clearance Canada-to-U.S. Ground Disbursement Fee: if customs value is $800 or less, the fee is the greater of $4.50 or 2% of Duty, Tax, and Merchandise Processing Fee. If customs value exceeds $800, the fee is the greater of $14 or 2%.",
    "Clearance Canada-to-U.S. Ground Duty and Tax Forwarding Fee: if customs value is $800 or less, the fee is $8.50 or 2% of Duty and Tax, whichever is greater. If customs value exceeds $800, the fee is $27 or 2% of Duty and Tax, whichever is greater.",

    # ── Change of Air Waybill ─────────────────────────────────────────────────
    "Change of Air Waybill Charge for FedEx International Premium is $6.50 per shipment.",

    # ── Dangerous Goods ───────────────────────────────────────────────────────
    "Dangerous Goods surcharge for FedEx First Overnight or FedEx Priority Overnight accessible is $175.00 per package.",
    "Dangerous Goods surcharge for FedEx First Overnight or FedEx Priority Overnight inaccessible is $80.00 per package.",
    "Dangerous Goods dry ice surcharge for FedEx First Overnight or FedEx Priority Overnight is $8.00 per package.",
    "Dangerous Goods surcharge for FedEx Standard Overnight, 2Day AM, 2Day, or Express Saver inaccessible is $80.00 per package.",
    "Dangerous Goods dry ice surcharge for FedEx Standard Overnight, 2Day AM, 2Day, or Express Saver is $8.00 per package.",
    "Dangerous Goods surcharge for International accessible (FedEx International First, Priority Express, Priority, Economy) is the greater of $240.00 per shipment or $1.40 per lb.",
    "Dangerous Goods surcharge for International inaccessible (FedEx International First, Priority Express, Priority, Economy) is the greater of $115.00 per shipment or $0.67 per lb.",
    "Dangerous Goods dry ice for International shipments or shipments to Puerto Rico is $8.00 per shipment.",
    "Dangerous Goods surcharge for FedEx First Overnight Freight or 1Day Freight accessible is the greater of $175.00 per shipment or $1.40 per lb.",
    "Dangerous Goods surcharge for FedEx First Overnight Freight or 1Day Freight inaccessible is the greater of $145.00 per shipment or $0.50 per lb.",
    "Dangerous Goods surcharge for FedEx 2Day Freight or 3Day Freight inaccessible is the greater of $145.00 per shipment or $0.50 per lb.",
    "Dangerous Goods surcharge for International Express Freight accessible is the greater of $255.00 per shipment or $1.40 per lb.",
    "Dangerous Goods surcharge for International Express Freight inaccessible is the greater of $145.00 per shipment or $0.67 per lb.",
    "Hazmat surcharge for FedEx Ground is $54.00.",
    "Hazmat surcharge for FedEx Home Delivery or International Ground Limited Quantity is $0.",

    # ── Declared Value ────────────────────────────────────────────────────────
    "Declared Value surcharge for U.S. packages: $4.50 for shipments valued between $100.01 and $300.00, then $1.50 per $100 for values over $300.",
    "Declared Value surcharge for International packages is $1.50 per $100 of value in excess of $100, or $9.07 per lb, whichever is greater.",
    "Declared Value surcharge for U.S. Express Freight is $1.50 per $100 of value in excess of $100, or $1.00 per lb, whichever is greater.",

    # ── Delivery Area Surcharge ───────────────────────────────────────────────
    "Delivery Area Surcharge for Commercial is $4.20.",
    "Delivery Area Surcharge for Extended Commercial is $5.25.",
    "Delivery Area Surcharge for Residential is $6.20.",
    "Delivery Area Surcharge for Extended Residential is $8.30.",
    "Delivery Area Surcharge for Remote (Commercial and Residential) is $15.50.",
    "Delivery Area Surcharge for Hawaii is $14.50.",
    "Delivery Area Surcharge for Alaska (Commercial and Residential) is $43.00.",

    # ── Delivery Reattempt ────────────────────────────────────────────────────
    "Delivery Reattempt fee for U.S. Express Freight is the greater of $91.50 per shipment or $0.100 per lb.",

    # ── EEI Filing ────────────────────────────────────────────────────────────
    "EEI (Electronic Export Information) Filing fee is $13.00.",

    # ── Extended Service Area (Express Freight) ───────────────────────────────
    "Extended Service Area Delivery surcharge for U.S. Express Freight is $245.00.",
    "Extended Service Area Pickup surcharge for U.S. Express Freight is $245.00.",

    # ── Extra Services / Special Handling ────────────────────────────────────
    "Extra Services Charge (Special Handling) for U.S. Express Freight is $135.00 per handler per hour.",

    # ── Delivery Manager ──────────────────────────────────────────────────────
    "Delivery Manager Hold at Location for specific date is $5.55.",
    "Delivery Manager Hold at FedEx location specific date and time is $11.50.",
    "Delivery Manager redirect within 120 miles fee is $5.55.",
    "Delivery Manager redirect over 120 miles next day fee is $33.50.",
    "Delivery Manager redirect over 120 miles 3 days later fee is $22.50.",
    "Delivery Manager redirect for Ground or Home Delivery is $14.50.",
    "Delivery Manager First Overnight redirect fee is $0.",

    # ── Return Manager / Call Tag ─────────────────────────────────────────────
    "FedEx Email Return Label or Print Return Label fee for Express or Ground is $1.05 per label.",
    "FedEx Ground Call Tag for commercial pickup via electronic shipping solutions is $8.30 per package.",
    "FedEx Ground Call Tag for residential pickup is $9.50 per package.",
    "FedEx ExpressTag fee is $8.30 per package.",
    "Return Pickup (Billable Stamps) fee for FedEx Priority Overnight, Standard Overnight, 2Day AM, or 2Day is $4.00 per package.",

    # ── Signature Options ─────────────────────────────────────────────────────
    "Indirect Signature Required fee is $7.15 per package.",
    "Direct Signature Required fee is $7.15 per package.",
    "Adult Signature Required fee is $8.65 per package.",
    "Signature Indirect maximum multiweight charge is $50.05 per shipment.",
    "Signature Direct maximum multiweight charge is $50.05 per shipment.",
    "Signature Adult maximum multiweight charge is $60.55 per shipment.",
    "Signature Proof of Delivery fee is $6.00.",

    # ── Home Delivery Convenient Delivery Options ─────────────────────────────
    "Home Delivery Date Certain fee is $4.65 per shipment.",
    "Home Delivery Evening fee is $10.50 per shipment.",
    "Home Delivery Appointment fee is $24.00 per shipment.",

    # ── International Controlled Export ──────────────────────────────────────
    "International Controlled Export fee is $50.00 per shipment.",

    # ── On Demand Care ────────────────────────────────────────────────────────
    "On Demand Care for U.S. packages is the greater of $100.00 per package or $2.75 per lb.",
    "On Demand Care for International packages is the greater of $170.00 per shipment or $3.40 per lb.",
    "On Demand Care for U.S. Express Freight is the greater of $540.00 per freight handling unit or $1.02 per lb.",
    "On Demand Care for International Priority Freight or International Economy Freight is the greater of $690.00 per shipment or $0.69 per lb.",

    # ── Priority Alert ────────────────────────────────────────────────────────
    "FedEx Priority Alert for U.S. packages is $17.00 per package.",
    "FedEx Priority Alert for U.S. Express Freight is $170.00 per freight handling unit.",
    "FedEx Priority Alert for International First or International Priority is the greater of $28.50 per shipment or $0.57 per lb.",
    "FedEx Priority Alert for International Priority Freight is the greater of $230.00 per shipment or $0.23 per lb.",
    "FedEx Priority Alert Plus for U.S. packages is the greater of $19.75 or $0.56 per lb.",
    "FedEx Priority Alert Plus for U.S. Express Freight is the greater of $199.00 per freight handling unit or $0.34 per lb.",
    "FedEx Priority Alert Plus for International First or International Priority is the greater of $34.00 per shipment or $0.68 per lb.",
    "FedEx Priority Alert Plus for International Priority Freight is the greater of $290.00 per shipment or $0.29 per lb.",

    # ── Fuel Surcharge ────────────────────────────────────────────────────────
    "Fuel Surcharge is dynamic and changes weekly. Check fedex.com for the current rate.",

    ## ── Inside Delivery / Pickup ─────────────────────────────────────────────
    "Inside Delivery fee is $150.50 or $0.099 per lb, whichever is greater.",
    "Inside Pickup fee is $150.50 or $0.099 per lb, whichever is greater.",
    "Inside Delivery fee for U.S. Express Freight is the greater of $150.50 per shipment or $0.099 per lb.",
    "Inside Pickup fee for U.S. Express Freight is the greater of $150.50 per shipment or $0.099 per lb.",

    # ── Out of Delivery Area (International) ─────────────────────────────────
    "Out-of-Delivery-Area surcharge for International packages Tier A is $4.20 per shipment.",
    "Out-of-Delivery-Area surcharge for International packages Tier B is the greater of $49.00 per shipment or $0.49 per lb.",
    "Out-of-Delivery-Area surcharge for International packages Tier C is the greater of $64.00 per shipment or $0.64 per lb.",
    "Out-of-Delivery-Area surcharge for International freight Tier B is $245.00 per shipment.",
    "Out-of-Delivery-Area surcharge for International freight Tier C is $320.00 per shipment.",

    # ── Out of Pickup Area (International) ───────────────────────────────────
    "Out-of-Pickup-Area surcharge for International packages Tier A is $4.20 per shipment.",
    "Out-of-Pickup-Area surcharge for International packages Tier B is the greater of $49.00 per shipment or $0.49 per lb.",
    "Out-of-Pickup-Area surcharge for International packages Tier C is the greater of $64.00 per shipment or $0.64 per lb.",
    "Out-of-Pickup-Area surcharge for International freight Tier B is $245.00 per shipment.",
    "Out-of-Pickup-Area surcharge for International freight Tier C is $320.00 per shipment.",

    # ── Metro Service Area ────────────────────────────────────────────────────
    "Metro Service Area Delivery fee for U.S. Express Freight is $245.00.",
    "Metro Service Area Pickup fee for U.S. Express Freight is $245.00.",

    # ── Missing Account Number ────────────────────────────────────────────────
    "Missing or Invalid Account Number fee is $24.00 per shipment.",

    # ── Northern Canada ───────────────────────────────────────────────────────
    "Northern Canada surcharge for Yukon, Northwest Territories, Nunavut, or Labrador: packages weighing 70 lbs or less is $105.00.",
    "Northern Canada surcharge for Yukon, Northwest Territories, Nunavut, or Labrador: packages weighing more than 70 lbs (if accepted) is $165.00.",
    "Yukon surcharge for packages 70 lbs or less is $105.00.",
    "Nunavut surcharge for packages 70 lbs or less is $105.00.",
    "Northwest Territories surcharge for packages 70 lbs or less is $105.00.",
    "Labrador surcharge for packages 70 lbs or less is $105.00.",

    # ── Payer Rebilling ───────────────────────────────────────────────────────
    "Payer Rebilling fee is $24.00 per shipment.",

    # ── International Premium Pickup ──────────────────────────────────────────
    "International Premium Pickup minimum fee is $20.00.",
    "International Premium Pickup for 100 to 220 lbs is $0.16 per lb.",
    "International Premium Pickup for 221 to 660 lbs is $0.14 per lb.",
    "International Premium Pickup for 661 lbs and over is $0.12 per lb.",

    # ── Reroute ───────────────────────────────────────────────────────────────
    "Reroute fee for packages is $24.00.",
    "Reroute fee for U.S. Express Freight is $130.00.",

    # ── Residential Delivery ──────────────────────────────────────────────────
    "Residential Delivery surcharge for U.S. Express Package services is $6.55 per package.",
    "Residential Delivery surcharge for FedEx Ground, Home Delivery, or International Ground is $5.95 per package.",
    "Residential Delivery surcharge for International packages to Canada or U.S. import is $6.55 per shipment.",
    "Residential freight surcharge for U.S. Express Freight is $215.00 per shipment.",
    "Residential freight surcharge for International Priority Freight, International Economy Freight, or International Deferred Freight is $215.00 per shipment.",
    "Residential surcharge for delivering to a house via U.S. Express Package is $6.55.",
    "House delivery residential surcharge for Ground or Home Delivery is $5.95.",
    "Residential Delivery Multiweight maximum for Express is $58.95 per shipment.",
    "Residential Delivery Multiweight maximum for Ground is $53.55 per shipment.",

    # ── Saturday Delivery ─────────────────────────────────────────────────────
    "Saturday Delivery fee for FedEx First Overnight, Priority Overnight, Standard Overnight, or 2Day packages is $16.00.",
    "Saturday Delivery fee for FedEx International Priority Express or International Priority packages is $16.00 per shipment.",
    "Saturday Delivery fee for Express Freight or International Priority Freight is $210.00 per shipment.",
    "Saturday Delivery Priority Overnight fee is $16.00.",
    "Saturday Delivery First Overnight fee is $16.00.",

    # ── Saturday Pickup ───────────────────────────────────────────────────────
    "Saturday Expedited Processing (pickup) fee for U.S. packages is $16.00 per package.",
    "Saturday Pickup fee for U.S. Express Freight or International Express Freight is $210.00 per shipment.",
    "Saturday Pickup fee for International packages is $16.00 per shipment.",

    # ── SenseAware ────────────────────────────────────────────────────────────
    "SenseAware Domestic journey cost is $150.00.",
    "SenseAware International journey cost is $200.00.",
    "SenseAware NIST Certification fee is $15.00.",
    "SenseAware Probes fee is $25.00 per probe.",
    "SenseAware Late Fee is $10.00 per day.",
    "SenseAware Lost or Damaged Device fee is $350.00.",
    "SenseAware Lost or Damaged Dry Ice Probe fee is $130.00.",
    "SenseAware Lost or Damaged Cryogenic Probe fee is $175.00.",

    # ── Third Party Billing ───────────────────────────────────────────────────
    "Third Party Billing Surcharge is 5.0% of transportation charges, surcharges, and additional fees.",

    # ── U.S. Inbound Processing ───────────────────────────────────────────────
    "U.S. Inbound Processing fee for FedEx International First, Priority Express, Priority, Economy, or International Express Freight is $2.50 per shipment.",
    "U.S. Inbound Processing fee for FedEx International Connect Plus is $1.00 per shipment.",
    "U.S. Inbound Processing fee for FedEx International Ground is $2.50 per package.",
]
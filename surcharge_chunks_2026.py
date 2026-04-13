"""
STEP 4 — 185 hardcoded surcharge strings for FedEx 2026.
Manually verified against FedEx 2026 Service Guide pages 128-144.
DO NOT MODIFY these strings — they are the source of truth.
"""

SURCHARGE_CHUNKS = [
    # ── Additional Handling ───────────────────────────────────────────────────
    "Additional Handling surcharge for dimension: Zone 2 rate is $29.50.",
    "Additional Handling surcharge for dimension: Zones 3-4 rate is $32.75.",
    "Additional Handling surcharge for dimension: Zones 5-6 rate is $38.50.",
    "Additional Handling surcharge for dimension: Zones 7 and above rate is $40.75.",
    "Additional Handling surcharge for weight or packaging over 70 lbs: Zone 2 rate is $46.00.",
    "Additional Handling surcharge for weight or packaging over 70 lbs: Zones 3-4 rate is $50.25.",
    "Additional Handling surcharge for weight or packaging over 70 lbs: Zones 5-6 rate is $56.25.",
    "Additional Handling surcharge for weight or packaging over 70 lbs: Zones 7 and above rate is $58.75.",
    "Additional Handling surcharge for soft-sided packs is $40.00.",
    "Additional Handling surcharge for soft-sided packs minimum is $29.50.",
    "Additional Handling surcharge for international dimension: Zone 2 rate is $26.50.",
    "Additional Handling surcharge for international dimension: Zones 3-4 rate is $30.75.",
    "Additional Handling surcharge for international dimension: Zones 7 and above rate is $33.75.",
    "Additional Handling surcharge for U.S. Express Freight is $285.00.",
    "Additional Handling surcharge for U.S. Express Freight non-stackable is $360.00.",
    "Additional Handling surcharge for International Freight is $350.00.",
    # AHS alias
    "AHS (Additional Handling Surcharge) for dimension Zone 2 is $29.50.",
    "AHS (Additional Handling Surcharge) for dimension Zones 3-4 is $32.75.",
    "AHS (Additional Handling Surcharge) for dimension Zones 5-6 is $38.50.",
    "AHS (Additional Handling Surcharge) for dimension Zones 7+ is $40.75.",

    # ── Oversize ──────────────────────────────────────────────────────────────
    "Oversize charge for U.S. Package: Zone 2 rate is $255.00.",
    "Oversize charge for U.S. Package: Zones 3-4 rate is $275.00.",
    "Oversize charge for U.S. Package: Zones 5-6 rate is $320.00.",
    "Oversize charge for U.S. Package: Zones 7 and above rate is $330.00.",
    "Oversize charge for Home Delivery: Zone 2 rate is $255.00.",
    "Oversize charge for Home Delivery: Zones 3-4 rate is $275.00.",
    "Oversize charge for Home Delivery: Zones 5-6 rate is $320.00.",
    "Oversize charge for Home Delivery: Zones 7 and above rate is $330.00.",
    "Oversize charge for International packages is $208.00.",

    # ── Unauthorized Package ──────────────────────────────────────────────────
    "Unauthorized Package surcharge for International shipments is $700.00.",
    "Unauthorized Package surcharge for International Express Freight is $1,400.00.",
    "Unauthorized Package surcharge for U.S. packages is $1,875.00.",

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
    "International Saturday pickup is $112.00 per shipment.",

    # ── Pickup Area Surcharges ────────────────────────────────────────────────
    "Pickup Area surcharge Residential is $5.95.",
    "Pickup Area surcharge Pickup Area is $6.20.",
    "Pickup Area surcharge Extended Area is $8.30.",
    "Pickup Area surcharge Remote is $15.50.",

    # ── Address Correction ────────────────────────────────────────────────────
    "Address Correction surcharge for packages is $25.50.",
    "Address Correction surcharge for freight is $130.00.",
    "Address Correction Multiweight Ground maximum per shipment is $76.50.",
    "Address Correction Multiweight Express maximum per shipment is $178.50.",
    "Wrong address correction fee is $25.50 per package.",
    "Incorrect address fee is $25.50.",
    "Bad address correction surcharge is $25.50.",

    # ── Broker In-Bond Transfer ───────────────────────────────────────────────
    "Broker Document Transfer fee is $51.00.",
    "Broker In-Bond Transfer fee is $90.00.",

    # ── Clearance — U.S. Import ───────────────────────────────────────────────
    "Clearance U.S. Import Entry Copy fee is $2.10.",
    "Clearance U.S. Import Entry of Goods fee is $53.00.",
    "Clearance U.S. Import Live Entry fee is $28.00.",
    "Clearance U.S. Import Prior Notice Food fee is $14.00.",
    "Clearance U.S. Import storage fee is $0.08 per kg per day plus $20.00 base starting from the 3rd day.",
    "Clearance U.S. Import Duty and Tax Forwarding Fee: if customs value is $800 or less, the fee is the greater of $8.50 or 2% of Duty and Tax. If customs value exceeds $800, the fee is the greater of $27 or 2% of Duty and Tax.",

    # ── Clearance — Temporary Import ─────────────────────────────────────────
    "Clearance Temporary Import fee is $150.00.",

    # ── Clearance — Government Agencies ──────────────────────────────────────
    "Clearance ATF (Bureau of Alcohol Tobacco Firearms) fee is $74.00.",
    "Clearance FWS (Fish and Wildlife Service) fee is government fees plus $23.00.",
    "Clearance FDA fee is $29.00.",
    "Clearance Additional Lines fee is $3.50 per line.",

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
    "Clearance Canada disbursement fee is CAD$11.40 or 2.95% whichever is greater.",
    "Clearance Canada Temporary Import fee is CAD$120.00.",
    "Clearance Canada OGA (Other Government Agency) fee is CAD$16.50.",
    "Clearance Canada Fax fee is CAD$3.00.",
    "Clearance Canada Call fee is CAD$4.00.",

    # ── Clearance — Canada to U.S. ────────────────────────────────────────────
    "Clearance Canada-to-U.S. shipment value $0 to $200.00: fee is $9.75.",
    "Clearance Canada-to-U.S. shipment value $200.01 to $800.00: fee is $19.50.",
    "Clearance Canada-to-U.S. shipment value $800.01 to $1250.00: fee is $30.50.",
    "Clearance Canada-to-U.S. shipment value $1250.01 to $2000.00: fee is $42.25.",
    "Clearance Canada-to-U.S. shipment value over $2000.00: fee is $42.25 plus $1.95 per additional $1000.",
    "Clearance Canada-to-U.S. Ground Disbursement Fee: if customs value is $800 or less, the fee is the greater of $4.50 or 2% of Duty, Tax, and Merchandise Processing Fee. If customs value exceeds $800, the fee is the greater of $14 or 2%.",
    "Clearance Canada-to-U.S. Ground Duty and Tax Forwarding Fee: if customs value is $800 or less, the fee is $8.50 or 2% of Duty and Tax, whichever is greater. If customs value exceeds $800, the fee is $27 or 2% of Duty and Tax, whichever is greater.",

    # ── Change of Air Waybill ─────────────────────────────────────────────────
    "Change of Air Waybill Charge for FedEx International Premium is $6.50 per shipment.",

    # ── Dangerous Goods ───────────────────────────────────────────────────────
    "Dangerous Goods dry ice surcharge for FedEx First Overnight or FedEx Priority Overnight is $8.00 per package.",
    "Dangerous Goods dry ice surcharge for FedEx Standard Overnight, 2Day AM, 2Day, or Express Saver is $8.00 per package.",
    "Dangerous Goods surcharge for International accessible is $240.00 or $1.48 per lb, whichever is greater.",
    "Dangerous Goods surcharge for International inaccessible is $115.00 or $0.71 per lb, whichever is greater.",
    "Dangerous Goods dry ice Puerto Rico surcharge is $8.50.",
    "Dangerous Goods surcharge for First Overnight Freight accessible is $185.00 or $1.48 per lb.",
    "Dangerous Goods surcharge for First Overnight Freight inaccessible is $153.50 or $0.53 per lb.",
    "Dangerous Goods surcharge for 2Day or 3Day Freight inaccessible is $153.50 or $0.53 per lb.",
    "Dangerous Goods surcharge for International Express Freight accessible is $270.00 or $1.48 per lb.",
    "Dangerous Goods surcharge for International Express Freight inaccessible is $153.50 or $0.71 per lb.",
    "Hazmat surcharge for Ground is $57.25.",
    "Hazmat surcharge for Home Delivery or International Ground Limited Quantity is $0.",

    # ── Declared Value ────────────────────────────────────────────────────────
    "Declared Value surcharge for packages and international is $1.65 per $100 declared value over $100.",
    "Declared Value surcharge for freight is $1.65 per $100 or $1.00 per lb, whichever is greater.",

    # ── Delivery Area Surcharge ───────────────────────────────────────────────
    "Delivery Area Surcharge for Commercial is $4.45.",
    "Delivery Area Surcharge for Extended Commercial is $8.80.",
    "Delivery Area Surcharge for Residential is $6.60.",
    "Delivery Area Surcharge for Extended Residential is $8.80.",
    "Delivery Area Surcharge for Remote is $22.25 to $44.00 depending on tier.",
    "Delivery Area Surcharge for Hawaii is $16.25.",

    # ── Delivery Reattempt ────────────────────────────────────────────────────
    "Delivery Reattempt fee for Express Freight is $97.00 or $0.106 per lb, whichever is greater.",

    # ── EEI Filing ────────────────────────────────────────────────────────────
    "EEI Filing fee is $13.00.",

    # ── Extended Delivery / Pickup Area (Express Freight) ─────────────────────
    "Extended Delivery Area surcharge for Express Freight is $260.00.",
    "Extended Pickup Area surcharge for Express Freight is $260.00.",

    # ── Special Handling ──────────────────────────────────────────────────────
    "Special Handling fee is $145.00 per handler per hour.",

    # ── Delivery Manager ──────────────────────────────────────────────────────
    "Delivery Manager Hold at Location for specific date is $5.55.",
    "Delivery Manager Hold at FedEx location is $11.50.",
    "Delivery Manager redirect within 120 miles fee is $5.55.",
    "Delivery Manager redirect over 120 miles next day fee is $33.50.",
    "Delivery Manager redirect over 120 miles 3 days later fee is $22.50.",
    "Delivery Manager redirect for Ground or Home Delivery is $14.50.",
    "Delivery Manager First Overnight redirect fee is $0.",

    # ── Return Manager / Call Tag ─────────────────────────────────────────────
    "Return Manager or Call Tag for First Overnight or International is $1.05.",
    "Return Manager or Call Tag for Ground commercial is $8.80.",
    "Return Manager or Call Tag for Ground residential is $10.00.",
    "FedEx ExpressTag fee is $8.30 per package.",
    "Return Pickup (Billable Stamps) fee for FedEx Priority Overnight, Standard Overnight, 2Day AM, or 2Day is $4.00 per package.",

    # ── Signature Options ─────────────────────────────────────────────────────
    "Indirect Signature Required fee is $7.60 per package.",
    "Direct Signature Required fee is $7.60 per package.",
    "Adult Signature Required fee is $10.00 per package.",
    "Signature Indirect maximum is $53.20.",
    "Signature Direct maximum is $53.20.",
    "Signature Adult maximum is $70.00.",
    "Signature Proof of Delivery fee is $6.00.",

    # ── Home Delivery Special Services ───────────────────────────────────────
    "Home Delivery Date Certain fee is $4.95.",
    "Home Delivery Evening fee is $11.25.",
    "Home Delivery Appointment fee is $25.50.",

    # ── International Controlled Export ──────────────────────────────────────
    "International Controlled Export fee is $50.00.",

    # ── On Demand Care ────────────────────────────────────────────────────────
    "On Demand Care for U.S. packages is $100.00 or $2.75 per lb, whichever is greater.",
    "On Demand Care for International is $170.00 or $3.40 per lb, whichever is greater.",
    "On Demand Care for U.S. Express Freight is $540.00 or $1.02 per lb, whichever is greater.",
    "On Demand Care for International Priority Freight is $690.00 or $0.69 per lb, whichever is greater.",

    # ── Priority Alert ────────────────────────────────────────────────────────
    "PriorityAlert for International First or International Priority is $30.05 or $0.60 per lb.",
    "PriorityAlert for International Priority Freight is $240.00 or $0.24 per lb.",
    "PriorityAlert for U.S. Express Freight is $180.00.",
    "PriorityAlert Plus for International First or International Priority is $36.00 or $0.72 per lb.",
    "PriorityAlert Plus for International Priority Freight is $310.00 or $0.31 per lb.",
    "PriorityAlert Plus for U.S. Express Freight is $210.75 or $0.36 per lb.",

    # ── Fuel Surcharge ────────────────────────────────────────────────────────
    "Fuel Surcharge is dynamic and changes weekly. Check fedex.com for the current rate.",

    # ── Inside Delivery / Pickup ─────────────────────────────────────────────
    "Inside Delivery fee is $160.00 or $0.105 per lb, whichever is greater.",
    "Inside Pickup fee is $160.00 or $0.105 per lb, whichever is greater.",

    # ── Out of Delivery Area (International) ─────────────────────────────────
    "Out-of-Delivery-Area surcharge for International packages Tier A is $4.45.",
    "Out-of-Delivery-Area surcharge for International packages Tier B is $49.00 or $0.52 per lb.",
    "Out-of-Delivery-Area surcharge for International packages Tier C is $68.00 or $0.68 per lb.",
    "Out-of-Delivery-Area surcharge for International freight Tier B is $260.00.",
    "Out-of-Delivery-Area surcharge for International freight Tier C is $340.00.",

    # ── Out of Pickup Area (International) ───────────────────────────────────
    "Out-of-Pickup-Area surcharge for International packages Tier A is $4.45.",
    "Out-of-Pickup-Area surcharge for International packages Tier B is $49.00 or $0.52 per lb.",
    "Out-of-Pickup-Area surcharge for International packages Tier C is $68.00 or $0.68 per lb.",
    "Out-of-Pickup-Area surcharge for International freight Tier B is $260.00.",
    "Out-of-Pickup-Area surcharge for International freight Tier C is $340.00.",

    # ── Metro Service Area ────────────────────────────────────────────────────
    "Metro Service Area Delivery fee is $260.00.",
    "Metro Service Area Pickup fee is $260.00.",

    # ── Missing Account Number ────────────────────────────────────────────────
    "Missing Account Number fee is $25.50.",

    # ── Northern Canada ───────────────────────────────────────────────────────
    "Northern Canada surcharge for Yukon, Northwest Territories, Nunavut, or Labrador: 70 lbs or less is $110.00.",
    "Northern Canada surcharge for Yukon, Northwest Territories, Nunavut, or Labrador: over 70 lbs is $175.00.",
    "Yukon surcharge 70 lbs or less is $110.00.",
    "Nunavut surcharge 70 lbs or less is $110.00.",
    "Northwest Territories surcharge 70 lbs or less is $110.00.",
    "Labrador surcharge 70 lbs or less is $110.00.",

    # ── Payer Rebilling ───────────────────────────────────────────────────────
    "Payer Rebilling fee is $25.50.",

    # ── International Premium Pickup ──────────────────────────────────────────
    "International Premium Pickup minimum fee is $20.00.",
    "International Premium Pickup for 100 to 220 lbs is $0.16 per lb.",
    "International Premium Pickup for 221 to 660 lbs is $0.14 per lb.",
    "International Premium Pickup for 661 lbs and over is $0.12 per lb.",

    # ── Reroute ───────────────────────────────────────────────────────────────
    "Reroute fee for packages is $25.50.",
    "Reroute fee for freight is $130.00.",

    # ── Residential Delivery ──────────────────────────────────────────────────
    "Residential Delivery surcharge for Home Delivery is $6.45.",
    "Residential Delivery surcharge for U.S. Package or International is $6.95.",
    "Residential Delivery Multiweight maximum per shipment is $62.55.",
    "Residential freight surcharge for U.S. Express Freight or International Priority Freight is $230.00.",
    "Residential surcharge for delivering to a house is $6.95.",
    "House delivery residential surcharge is $6.95.",

    # ── Saturday Delivery ─────────────────────────────────────────────────────
    "Saturday Delivery fee for packages is $16.00.",
    "Saturday Delivery fee for International Priority Express or International Priority packages is $16.00.",
    "Saturday Delivery fee for freight is $210.00.",
    "Saturday Delivery Priority Overnight fee is $16.00.",
    "Saturday Delivery First Overnight fee is $16.00.",
    "Saturday Delivery Standard Overnight fee is $16.00.",

    # ── Saturday Pickup ───────────────────────────────────────────────────────
    "Saturday Pickup fee for packages is $16.00.",
    "Saturday Pickup fee for freight is $210.00.",
    "Saturday Pickup fee for International packages is $16.00.",

    # ── SenseAware ────────────────────────────────────────────────────────────
    "SenseAware Domestic journey cost is $150.00.",
    "SenseAware International journey cost is $200.00.",
    "SenseAware NIST Certification fee is $15.00.",
    "SenseAware Probes fee is $25.00.",
    "SenseAware Late Fee is $10.00 per day.",
    "SenseAware Lost Device fee is $350.00.",
    "SenseAware Lost Dry Ice Probe fee is $130.00.",
    "SenseAware Lost Cryogenic Probe fee is $175.00.",

    # ── Third Party Billing ───────────────────────────────────────────────────
    "Third Party Billing fee is 5% of the transportation charges.",

    # ── U.S. Inbound Processing ───────────────────────────────────────────────
    "U.S. Inbound Processing fee for International or Express Freight is $2.65.",
    "U.S. Inbound Processing fee for International Connect Plus is $1.00.",
    "U.S. Inbound Processing fee for International Ground is $2.65 per package.",

    # ── Missing Account ───────────────────────────────────────────────────────
    "Missing Account Number surcharge is $25.50.",
]
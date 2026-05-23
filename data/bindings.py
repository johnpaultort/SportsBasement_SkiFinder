import json

# ────────────────────────────────────────────────────────────
#  SNOWBOARD BINDINGS
#  styles options : "all-mountain" | "freeride" | "freestyle" | "carving"
#  shape options  : "directional" | "directional-twin" | "true-twin"
#  flex           : 1 (softest) – 10 (stiffest)
# ────────────────────────────────────────────────────────────

SB_BINDINGS = [
    # Union Bindings
    {
        "name":     "Strata",
        "brand":    "Union",
        "style":   ["all-mountain", "freestyle"],
        "skill":   ["beginner", "intermediate", "advanced"],
        "flex":     5,
        "pattern": ["4x2", "channel"],
        "price":    279.95,
        "image":    "https://unionbindingcompany.com/cdn/shop/files/UN25_STRATA_BLACK_1024x.jpg?v=1753686597",
        "notes":    "The Strata has a mini disk that allows the binding to carry a soft surfy feeling. Smaller contact point and allows your board to flex naturally."
    },
    {
        "name":      "Force",
        "brand":     "Union",
        "style":    ["all-mountain"],
        "skill":    ["beginner", "intermediate", "advanced"],
        "flex":      7, 
        "pattern":  ["4x4", "4x2", "channel"],
        "price":     349.95,
        "image":     "https://unionbindingcompany.com/cdn/shop/files/UN25_FORCE_BLACK_db5dd6ad-dca0-4136-982f-dfaf63159e12_1024x.jpg?v=1753861019",
        "notes":      "."
    },
    {
        "name":     "Falcor",
        "brand":    "Union",
        "style":    ["freeride"],
        "skill":    ["intermediate", "advanced"],
        "flex":     7,
        "pattern":  ["4x2", "channel"],
        "price":    439.95,
        "image":    "https://unionbindingcompany.com/cdn/shop/files/UN25_FALCOR_BLACK_1024x.jpg?v=1753276224",
        "notes":    "."
    },
    {
        "name":     "Atlas",
        "brand":    "Union",
        "style":    ["all-mountain", "carving"],
        "skill":    ["intermediate", "advanced"],
        "flex":     8,
        "pattern":  ["4x4", "4x2", "channel"],
        "price":    399.95,
        "image":    "https://unionbindingcompany.com/cdn/shop/files/UN25_ATLAS_CHROME_1024x.jpg?v=1757931696",
        "notes":    "."
    },
    {
        "name":     "Ultra",
        "brand":    "Union",
        "style":    ["freestyle", "all-mountain"],
        "skill":    ["beginner", "intermediate", "advanced"],
        "flex":     6, 
        "pattern":  ["4x2", "channel"],
        "price":    329.95,
        "image":    "https://unionbindingcompany.com/cdn/shop/files/UN25_ULTRA_BLACK_1024x.jpg?v=1753276418",
        "notes":    "."
    }            
]

SKI_BINDINGS = [
    # Pivots
    {
        "name": "Pivot 11",
        "brand": "Look",
        "widths":    [95, 105, 115],
        "price":    279.95,
        "image": "https://www.sportsbasement.com/cdn/shop/files/100288955_WHBK_1.png?v=1754107554",
        "notes": ""
    },
    {
        "name": "Pivot 13",
        "brand": "Look",
        "widths": [95, 105, 115],
        "price": 379.95,
        "image": "https://www.sportsbasement.com/cdn/shop/files/100288954_ORGM_1.png?crop=center&height=800&v=1754107555&width=800",
        "notes": ""
    },
    {
        "name": "Pivot 15",
        "brand": "Look",
        "widths": [95, 105, 115],
        "price": 479.95,
        "image": "https://www.sportsbasement.com/cdn/shop/files/100270601_ORMT_1.png?crop=center&height=800&v=1754107675&width=800",
        "notes": ""
    },
    # Marker        
    {
        "name": "Squire 11",
        "brand": "Marker",
        "widths": [90, 100, 110, 120],
        "price": 249.99,
        "image": "https://www.sportsbasement.com/cdn/shop/files/100224158_BLK_1.png?crop=center&height=800&v=1754107711&width=800",
        "notes": ""
    },
    {
        "name": "Jester 16 x MWerks",
        "brand": "Marker",
        "widths": [90, 100, 110, 120],
        "price": 489.99,
        "image": "https://www.sportsbasement.com/cdn/shop/files/100293342_BKOR_1.png?v=1754107226",
        "notes": ""
    }, 
    {
        "name": "Griffon 13",
        "brand": "Marker",
        "widths": [90, 100, 110, 120],
        "price": 299.99,
        "image": "https://www.sportsbasement.com/cdn/shop/files/100266735_BLK_1.png?crop=center&height=800&v=1750620997&width=800",
        "notes": ""
    }, 
    {
        "name": "Griffon 13 X",
        "brand": "Marker",
        "widths": [90, 100, 110, 120],
        "price": 429.99,
        "image": "https://www.sportsbasement.com/cdn/shop/files/100293343_BKGP_1.png?v=1754107225",
        "notes": ""
    },
    # Salomon
    {
        "name": "Strive 10 GW",
        "brand": "Salomon",
        "widths": [80, 90, 100],
        "price": 169.95,
        "image": "https://www.sportsbasement.com/cdn/shop/files/L47320500__0c5a9dbca60d4437c35d372eec9fb188.png?crop=center&height=800&v=1754107708&width=800",
        "notes": "."
    },
    {
        "name": "Strive 12 GW",
        "brand": "Salomon",
        "widths": [90, 100, 115],
        "price": 239.95,
        "image": "https://www.sportsbasement.com/cdn/shop/files/L47322700__7b8bea2180fdecdd09906e0759d0434b.png?crop=center&height=800&v=1754107706&width=800",
        "notes": "."
    },  
    {
        "name": "Strive 14 GW",
        "brand": "Salomon",
        "widths": [90, 100, 115, 130],
        "price": 279.95,
        "image": "https://www.sportsbasement.com/cdn/shop/files/100248134_BLK_1.png?v=1746656803",
        "notes": "."
    },  
    {
        "name": "Strive 16 MN",
        "brand": "Salomon",
        "widths": [90, 100, 115, 130],
        "price": 399.95,
        "image": "https://www.sportsbasement.com/cdn/shop/files/100248133-BLK-1.png?crop=center&height=800&v=1683821506&width=800",
        "notes": "."
    }  
]
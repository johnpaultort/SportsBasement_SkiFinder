import json

# ────────────────────────────────────────────────────────────
#  SNOWBOARD BINDINGS
#  styles options : "all-mountain" | "freeride" | "freestyle" | "carving"
#  shape options  : "directional" | "directional-twin" | "true-twin"
#  flex           : 1 (softest) – 10 (stiffest)
# ────────────────────────────────────────────────────────────

# Union sizing chart 
#
#         "sizes": [
#            {
#                "size": "S",
#                "boot_sizes": "5.5-7.5"
#            },
#            {
#                "size": "M",
#                "boot_sizes": "8-10"
#            },
#            {
#                "size": "L",
#                "boot_sizes": "10.5-13"
#            }
#          ],

SB_BINDINGS = [
    #
    # Union Bindings
    # 25/26 images
    # Ultra and Strata no update only

    {
        "gender": "mens",
        "name":     "Strata",
        "brand":    "Union",
        "style":   ["freestyle", "all-mountain"],
        "skill":   ["beginner", "intermediate", "advanced"],
        "sizes": [
            {
                "size": "S",
                "boot_sizes": "5.5-7.5"
            },
            {
                "size": "M",
                "boot_sizes": "8-10"
            },
            {
                "size": "L",
                "boot_sizes": "10.5-13"
            }
        ],
        "flex":     5,
        "pattern": ["4x2", "channel"],
        "binding": "traditional",
        "price":    "279.95",
        "image":    "https://unionbindingcompany.com/cdn/shop/files/UN25_STRATA_BLACK_1024x.jpg?v=1753686597",
        "notes":    "The Strata has a mini disk that allows the binding to carry a soft surfy feeling. Smaller contact point and allows your board to flex naturally."
    },
    {
        "gender": "mens",
        "name":      "Force",
        "brand":     "Union",
        "style":    ["all-mountain", "freestyle"],
        "skill":    ["beginner", "intermediate", "advanced"],
        "sizes": [
            {
                "size": "S",
                "boot_sizes": "5.5-7.5"
            },
            {
                "size": "M",
                "boot_sizes": "8-10"
            },
            {
                "size": "L",
                "boot_sizes": "10.5-13"
            }
        ],
        "flex":      7, 
        "pattern":  ["4x4", "4x2", "channel"],
        "binding": "traditional",
        "price":     "349.95",
        "image":     "https://www.sportsbasement.com/cdn/shop/files/100303407.Force.Black.1.png?v=1780696910",
        "notes":      "."
    },
    # new image
    {
        "gender": "mens",
        "name":     "Falcor",
        "brand":    "Union",
        "style":    ["freeride", "freestyle", "all-mountain"],
        "skill":    ["intermediate", "advanced"],
        "sizes": [
            {
                "size": "S",
                "boot_sizes": "5.5-7.5"
            },
            {
                "size": "M",
                "boot_sizes": "8-10"
            },
            {
                "size": "L",
                "boot_sizes": "10.5-13"
            }
        ],
        "flex":     7,
        "pattern":  ["4x2", "channel"],
        "binding": "traditional",
        "price":    "439.95",
        "image":    "https://www.sportsbasement.com/cdn/shop/files/100303402.Black.1.png?v=1780676964",
        "notes":    "."
    },
    # new image
    {
        "gender": "mens",
        "name":     "Atlas",
        "brand":    "Union",
        "style":    ["all-mountain", "carving", "freestyle", "freeride"],
        "skill":    ["intermediate", "advanced"],
        "sizes": [
            {
                "size": "S",
                "boot_sizes": "5.5-7.5"
            },
            {
                "size": "M",
                "boot_sizes": "8-10"
            },
            {
                "size": "L",
                "boot_sizes": "10.5-13"
            }
        ],
        "flex":     8,
        "pattern":  ["4x4", "4x2", "channel"],
        "binding": "traditional",
        "price":    "399.95",
        "image":    "https://www.sportsbasement.com/cdn/shop/files/100303406.Atlas.Black.1.png?v=1780693194",
        "notes":    "."
    },
    # no update
    {
        "gender": "mens",
        "name":     "Ultra",
        "brand":    "Union",
        "style":    ["freestyle", "all-mountain"],
        "skill":    ["intermediate", "advanced"],
        "sizes": [
            {
                "size": "S",
                "boot_sizes": "5.5-7.5"
            },
            {
                "size": "M",
                "boot_sizes": "8-10"
            },
            {
                "size": "L",
                "boot_sizes": "10.5-13"
            }
        ],
        "flex":     6, 
        "pattern":  ["4x2", "channel"],
        "binding": "traditional",
        "price":    "329.95",
        "image":    "https://unionbindingcompany.com/cdn/shop/files/UN25_ULTRA_BLACK_1024x.jpg?v=1753276418",
        "notes":    "."
    },
    # new
    {
        "gender": "mens",
        "name":     "Neo",
        "brand":    "Union",
        "style":    ["freestyle", "all-mountain"],
        "skill":    ["beginner", "intermediate", "advanced"],
        "sizes": [
            {
                "size": "S",
                "boot_sizes": "5.5-7.5"
            },
            {
                "size": "M",
                "boot_sizes": "8-10"
            },
            {
                "size": "L",
                "boot_sizes": "10.5-13"
            }
        ],
        "flex":     6, 
        "pattern":  ["4x2", "channel"],
        "binding": "traditional",
        "price":    "379.95",
        "image":    "https://www.sportsbasement.com/cdn/shop/files/100303403.Neo.White.1.png?v=1780680369",
        "notes":    "."
    },
    # new
    {
        "gender": "mens",
        "name":     "STR",
        "brand":    "Union",
        "style":    ["all-mountain"],
        "skill":    ["beginner"],
        "sizes": [
            {
                "size": "S",
                "boot_sizes": "5.5-7.5"
            },
            {
                "size": "M",
                "boot_sizes": "8-10"
            },
            {
                "size": "L",
                "boot_sizes": "10.5-13"
            }
        ],
        "flex":     6, 
        "pattern":  ["4x2", "4x4", "channel"],
        "binding": "traditional", 
        "price":    "199.95",
        "image":    "https://www.sportsbasement.com/cdn/shop/files/100303408.STR.Black.1.png?v=1780704023",
        "notes":    "."
    },
    {
        "gender": "mens",
        "name":     "Atlas Step On",
        "brand":    "Union",
        "style":    ["freestyle", "all-mountain", "freeride"],
        "skill":    ["intermediate", "advanced"],
        "sizes": [
            {
                "size": "S",
                "boot_sizes": "6-8"
            },
            {
                "size": "M",
                "boot_sizes": "8.5-10.5"
            },
            {
                "size": "L",
                "boot_sizes": "11-13"
            },
            {
                "size": "XL",
                "boot_sizes": "14-15"
            }
        ],
        "flex":     8, 
        "pattern":  ["4x2", "channel"],
        "binding": "step-on",
        "price":    "429.95",
        "image":    "https://www.sportsbasement.com/cdn/shop/files/100303392.Black.1.png?v=1780506580",
        "notes":    "."
    },
    {
        "gender": "mens",
        "name":     "Atlas Step On Pro",
        "brand":    "Union",
        "style":    ["freestyle", "all-mountain"],
        "skill":    ["beginner", "intermediate", "advanced"],
        "sizes": [
            {
                "size": "S",
                "boot_sizes": "5.5-7.5"
            },
            {
                "size": "M",
                "boot_sizes": "8-10"
            },
            {
                "size": "L",
                "boot_sizes": "10.5-13"
            }
        ],
        "flex":     6, 
        "pattern":  ["4x2", "channel"],
        "binding": "step-on",
        "price":    "499.95",
        "image":    "https://www.sportsbasement.com/cdn/shop/files/100303385.Black.1.png?v=1780499173",
        "notes":    "."
    },
    {
        "gender": "mens",
        "name":     "Source",
        "brand":    "Union",
        "style":    ["all-mountain", "carving", "freeride"],
        "skill":    ["beginner", "intermediate", "advanced"],
        "sizes": [
            {
                "size": "M",
                "boot_sizes": "8-10"
            },
            {
                "size": "L",
                "boot_sizes": "10.5-13"
            }
        ],
        "flex":     7, 
        "pattern":  ["4x2", "channel"],
        "binding": "traditional",
        "price":    "549.95",
        "image":    "https://www.sportsbasement.com/cdn/shop/files/100303400.Source.Black.1.png?v=1780612051",
        "notes":    "."
    },
    {
        "gender": "mens",
        "name":     "Source FC",
        "brand":    "Union",
        "style":    ["all-mountain", "freeride", "carving"],
        "skill":    ["beginner", "intermediate", "advanced"],
        "sizes": [
            {
                "size": "M",
                "boot_sizes": "8-10"
            },
            {
                "size": "L",
                "boot_sizes": "10.5-13"
            }
        ],
        "flex":     8, 
        "pattern":  ["4x2", "channel"],
        "binding": "traditional",
        "price":    "999.95",
        "image":    "https://www.sportsbasement.com/cdn/shop/files/100303396.FCBlack.1.png?v=1780606599",
        "notes":    "."
    },
    {
        "gender": "mens",
        "name":     "Source Pro TH",
        "brand":    "Union",
        "style":    ["freestyle", "all-mountain"],
        "skill":    ["beginner", "intermediate", "advanced"],
        "sizes": [
            {
                "size": "M",
                "boot_sizes": "8-10"
            },
            {
                "size": "L",
                "boot_sizes": "10.5-13"
            }
        ],
        "flex":     6, 
        "pattern":  ["4x2", "channel"],
        "binding": "traditional", 
        "price":    "999.95",
        "image":    "https://www.sportsbasement.com/cdn/shop/files/100303397.SourceProTH.Black.1.png?v=1780610364",
        "notes":    "."
    },

    # 26/27 images
    # Jones Bindings
    {
        "gender": ["mens", "womens"],
        "name":     "Nebula FASE",
        "brand":    "Jones",
        "style":    ["freestyle", "all-mountain"],
        "skill":    ["beginner", "intermediate", "advanced"],
        "sizes": [
            {
                "size": "S",
                "boot_sizes": "5-8"
            },
            {
                "size": "M",
                "boot_sizes": "8.5-10.5"
            },
            {
                "size": "L",
                "boot_sizes": "11-14"
            }
        ],
        "flex":     4, 
        "pattern":  ["4x4", "4x2", "channel"],
        "binding": "fase",
        "price":    "299.95",
        "image":    "https://www.sportsbasement.com/cdn/shop/files/100308731_TBR_1.png?v=1780069215",
        "notes":    "."
    },
    {
        "gender": ["mens", "womens"],
        "name":     "Mercury FASE",
        "brand":    "Jones",
        "style":    ["freeride", "all-mountain"],
        "skill":    ["intermediate", "advanced"],
        "sizes": [
            {
                "size": "S",
                "boot_sizes": "5-8"
            },
            {
                "size": "M",
                "boot_sizes": "8.5-10.5"
            },
            {
                "size": "L",
                "boot_sizes": "11-14"
            }
        ],
        "flex":     8, 
        "pattern":  ["4x4", "4x2", "channel"],
        "binding": "fase",
        "price":    "369.95",
        "image":    "https://www.sportsbasement.com/cdn/shop/files/100308731_TBR_1.png?v=1780069215",
        "notes":    "."
    }
]

SKI_BINDINGS = [
    #
    # Pivots
    # 25/26 images
    {
        "name": "Pivot 11",
        "brand": "Look",
        "widths":[95, 105, 115],
        "price": "279.95",
        "image": "https://www.sportsbasement.com/cdn/shop/files/100288955_WHBK_1.png?v=1754107554",
        "notes": ""
    },
    {
        "name": "Pivot 13",
        "brand": "Look",
        "widths": [95, 105, 115],
        "price": "379.95",
        "image": "https://www.sportsbasement.com/cdn/shop/files/100288954_ORGM_1.png?crop=center&height=800&v=1754107555&width=800",
        "notes": ""
    },
    {
        "name": "Pivot 15",
        "brand": "Look",
        "widths": [95, 105, 115],
        "price": "479.95",
        "image": "https://www.sportsbasement.com/cdn/shop/files/100270601_ORMT_1.png?crop=center&height=800&v=1754107675&width=800",
        "notes": ""
    },
    # Marker        
    {
        "name": "Squire 11",
        "brand": "Marker",
        "widths": [90, 100, 110, 120],
        "price": "249.99",
        "image": "https://www.sportsbasement.com/cdn/shop/files/100224158_BLK_1.png?crop=center&height=800&v=1754107711&width=800",
        "notes": ""
    },
    {
        "name": "Jester 16 x MWerks",
        "brand": "Marker",
        "widths": [90, 100, 110, 120],
        "price": "489.99",
        "image": "https://www.sportsbasement.com/cdn/shop/files/100293342_BKOR_1.png?v=1754107226",
        "notes": ""
    }, 
    {
        "name": "Griffon 13",
        "brand": "Marker",
        "widths": [90, 100, 110, 120],
        "price": "299.99",
        "image": "https://www.sportsbasement.com/cdn/shop/files/100266735_BLK_1.png?crop=center&height=800&v=1750620997&width=800",
        "notes": ""
    }, 
    {
        "name": "Griffon 13 X",
        "brand": "Marker",
        "widths": [90, 100, 110, 120],
        "price": "299.99",
        "image": "https://www.sportsbasement.com/cdn/shop/files/100305309_BLK_1.png?v=1779991584",
        "notes": ""
    },
    # Salomon
    {
        "name": "Strive 10 GW",
        "brand": "Salomon",
        "widths": [80, 90, 100],
        "price": "169.95",
        "image": "https://www.sportsbasement.com/cdn/shop/files/L47320500__0c5a9dbca60d4437c35d372eec9fb188.png?crop=center&height=800&v=1754107708&width=800",
        "notes": "."
    },
    {
        "name": "Strive 12 GW",
        "brand": "Salomon",
        "widths": [90, 100, 115],
        "price": "239.95",
        "image": "https://www.sportsbasement.com/cdn/shop/files/L47322700__7b8bea2180fdecdd09906e0759d0434b.png?crop=center&height=800&v=1754107706&width=800",
        "notes": "."
    },  
    {
        "name": "Strive 14 GW",
        "brand": "Salomon",
        "widths": [90, 100, 115, 130],
        "price": "279.95",
        "image": "https://www.sportsbasement.com/cdn/shop/files/100248134_BLK_1.png?v=1746656803",
        "notes": "."
    },  
    {
        "name": "Strive 16 MN",
        "brand": "Salomon",
        "widths": [90, 100, 115, 130],
        "price": "399.95",
        "image": "https://www.sportsbasement.com/cdn/shop/files/100248133-BLK-1.png?crop=center&height=800&v=1683821506&width=800",
        "notes": "."
    }  
]
#Keywords with all the terms
TRACK_WORDS = ['COP26', 'cop26', 'Glasgow Climate Pact', 'glasgowclimateimpact', 'climate change', 'climatechange', 'globalwarming', 'global warming', \
            'carbon footprint', 'greenhouse effect', 'greenhouse gas', 'climaterealists', 'climate emergency', 'global net zero',\
            'net zero', 'netzero', 'zero emission', 'renewable energy', 'carbon dioxide', 'fossil fuel', 'environment', 'nature', 'savetheplanet', 'sustainability', 'climatecrisis', \
            'climatestrike', 'climateaction', 'climate hoax', 'climatehoax', 'climatechangeisreal', 'actonclimate', 'theclimateconnection' \
            'climateemergency', 'carbon', 'methane', 'parisagreement' 'emission', 'emissions', 'climatechangehoax', 'Conference of Parties', \
            'greenhouse gas emissions', 'GlasgowClimatePact', 'togetherforourplanet']

TABLE_NAME = "FullAnalysis"

TABLE_ATTRIBUTES = "id_str VARCHAR(255), created_at DATETIME, text VARCHAR(255), \
            polarity INT, subjectivity INT, user_created_at VARCHAR(255), user_location VARCHAR(255), \
            user_description VARCHAR(255), user_followers_count INT, longitude DOUBLE, latitude DOUBLE, \
            retweet_count INT, favorite_count INT"




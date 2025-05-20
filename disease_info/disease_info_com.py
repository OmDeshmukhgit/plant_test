"""
Disease information and treatment recommendations for plant leaf diseases.
"""

DISEASE_INFO = {
    0: {
        "en": {
            "name": "Apple Scab",
            "description": "Apple scab is a fungal disease that affects apple trees. It appears as dark, scaly lesions on leaves, fruit, and twigs.",
            "symptoms": [
                "Dark, scaly lesions on leaves",
                "Brown spots on fruit",
                "Premature leaf drop",
                "Twig lesions"
            ],
            "causes": [
                "Fungal infection (Venturia inaequalis)",
                "Wet, cool weather conditions",
                "Poor air circulation",
                "Infected plant debris"
            ],
            "treatments": [
                "Apply fungicides during early spring",
                "Remove and destroy infected leaves and fruit",
                "Improve air circulation through pruning",
                "Use resistant apple varieties",
                "Maintain proper tree spacing"
            ]
        },
        "hi": {
            "name": "सेब___स्कैब",
            "description": "सेब स्कैब एक फंगल रोग है जो सेब के पेड़ों को प्रभावित करता है। यह पत्तियों, फलों और टहनियों पर काले, पपड़ीदार धब्बों के रूप में दिखाई देता है।",
            "symptoms": [
                "पत्तियों पर काले, पपड़ीदार धब्बे",
                "फलों पर भूरे धब्बे",
                "समय से पहले पत्तियों का गिरना",
                "टहनियों पर धब्बे"
            ],
            "causes": [
                "फंगल संक्रमण (Venturia inaequalis)",
                "गीला, ठंडा मौसम",
                "खराब वायु संचार",
                "संक्रमित पौधों का मलबा"
            ],
            "treatments": [
                "वसंत ऋतु की शुरुआत में फफूंदनाशी का छिड़काव करें",
                "संक्रमित पत्तियों और फलों को हटाएं और नष्ट करें",
                "छंटाई के माध्यम से वायु संचार सुधारें",
                "प्रतिरोधी सेब किस्मों का उपयोग करें",
                "उचित पेड़ की दूरी बनाए रखें"
            ]
        },
        "mr": {
            "name": "सफरचंद___स्कॅब",
            "description": "सफरचंद स्कॅब हा एक बुरशीजन्य रोग आहे जो सफरचंदाच्या झाडांना प्रभावित करतो. हा पानांवर, फळांवर आणि फांद्यांवर काळे, खवलेदार डाग निर्माण करतो.",
            "symptoms": [
                "पानांवर काळे, खवलेदार डाग",
                "फळांवर तपकिरी डाग",
                "वेळीच पानगळ",
                "फांद्यांवर डाग"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Venturia inaequalis)",
                "ओलसर, थंड हवामान",
                "खराब हवेशीरता",
                "संक्रमित वनस्पती अवशेष"
            ],
            "treatments": [
                "वसंत ऋतूच्या सुरुवातीला बुरशीनाशक फवारणी करा",
                "संक्रमित पाने आणि फळे काढून टाका आणि नष्ट करा",
                "फांद्यांची छाटणी करून हवेशीरता वाढवा",
                "प्रतिरोधक सफरचंद जाती वापरा",
                "योग्य झाडांची अंतर ठेवावी"
            ]
        }
    },
    1: {
        "en": {
            "name": "Apple Black Rot",
            "description": "Black rot is a fungal disease that causes dark, circular lesions on leaves and fruit, leading to significant crop loss.",
            "symptoms": [
                "Dark, circular leaf spots",
                "Brown rot on fruit",
                "Cankers on branches",
                "Leaf yellowing and wilting"
            ],
            "causes": [
                "Fungal infection (Botryosphaeria obtusa)",
                "Warm, humid weather",
                "Wounds on plant tissue",
                "Infected plant material"
            ],
            "treatments": [
                "Prune infected branches",
                "Apply fungicides during growing season",
                "Remove infected fruit and leaves",
                "Maintain tree health through proper nutrition",
                "Improve air circulation"
            ]
        },
        "hi": {
            "name": "सेब___ब्लैक_रॉट",
            "description": "ब्लैक रॉट एक फंगल रोग है जो पत्तियों और फलों पर काले, गोल धब्बे बनाता है, जिससे फसल का भारी नुकसान हो सकता है।",
            "symptoms": [
                "पत्तियों पर काले, गोल धब्बे",
                "फलों पर ब्राउन रॉट",
                "टहनियों पर केंकर",
                "पत्तियों का पीला पड़ना और मुरझाना"
            ],
            "causes": [
                "फंगल संक्रमण (Botryosphaeria obtusa)",
                "गर्म, आर्द्र मौसम",
                "पौधों के ऊतक में घाव",
                "संक्रमित पौध सामग्री"
            ],
            "treatments": [
                "संक्रमित टहनियों की छंटाई करें",
                "विकास के मौसम में फफूंदनाशी का छिड़काव करें",
                "संक्रमित फल और पत्तियां हटाएं",
                "उचित पोषण द्वारा पेड़ का स्वास्थ्य बनाए रखें",
                "हवा का संचार सुधारें"
            ]
        },
        "mr": {
            "name": "सफरचंद___काळा_कुज",
            "description": "ब्लॅक रॉट हा एक बुरशीजन्य रोग आहे जो पानांवर आणि फळांवर काळे, गोल डाग निर्माण करतो, ज्यामुळे पिकाचे मोठे नुकसान होते.",
            "symptoms": [
                "पानांवर काळे, गोल डाग",
                "फळांवर ब्राउन रॉट",
                "फांद्यांवर कॅंकर",
                "पानांची पिवळसरता आणि मळमळ"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Botryosphaeria obtusa)",
                "उबदार, दमट हवामान",
                "वनस्पती ऊतींमध्ये जखमा",
                "संक्रमित वनस्पती साहित्य"
            ],
            "treatments": [
                "संक्रमित फांद्या छाटाव्यात",
                "वाढीच्या हंगामात बुरशीनाशक फवारणी करावी",
                "संक्रमित फळे आणि पाने काढून टाकावीत",
                "योग्य पोषणाने झाडाचे आरोग्य राखावे",
                "हवेशीरता वाढवावी"
            ]
        }
    },
    2: {
        "en": {
            "name": "Apple Cedar Apple Rust",
            "description": "Cedar apple rust is a fungal disease that requires both apple trees and cedar trees to complete its life cycle.",
            "symptoms": [
                "Bright orange-yellow spots on leaves",
                "Deformed fruit",
                "Early defoliation",
                "Reduced fruit quality"
            ],
            "causes": [
                "Fungal infection (Gymnosporangium juniperi-virginianae)",
                "Presence of cedar trees nearby",
                "Wet spring conditions",
                "Wind-blown spores"
            ],
            "treatments": [
                "Remove nearby cedar trees if possible",
                "Apply preventive fungicides",
                "Plant resistant apple varieties",
                "Maintain good air circulation",
                "Regular monitoring during spring"
            ]
        },
        "hi": {
            "name": "सेडर___सेब_रस्ट",
            "description": "सेडर-सेब रस्ट एक फंगल रोग है जिसके जीवन चक्र को पूरा करने के लिए सेब और देवदार दोनों पेड़ों की आवश्यकता होती है।",
            "symptoms": [
                "पत्तियों पर चमकीले नारंगी-पीले धब्बे",
                "विकृत फल",
                "समय से पहले पत्तियों का झड़ना",
                "फलों की गुणवत्ता में कमी"
            ],
            "causes": [
                "फंगल संक्रमण (Gymnosporangium juniperi-virginianae)",
                "आसपास देवदार के पेड़",
                "गीला वसंत मौसम",
                "हवा से उड़ने वाले बीजाणु"
            ],
            "treatments": [
                "संभव हो तो पास के देवदार के पेड़ हटाएं",
                "रोकथाम के लिए फफूंदनाशी का छिड़काव करें",
                "प्रतिरोधी सेब किस्में लगाएं",
                "अच्छा वायु संचार बनाए रखें",
                "वसंत के दौरान नियमित निगरानी करें"
            ]
        },
        "mr": {
            "name": "सिडर___सफरचंद_रस्ट",
            "description": "सिडर-सफरचंद रस्ट हा एक बुरशीजन्य रोग आहे ज्याच्या जीवनचक्रासाठी सफरचंद आणि सिडर दोन्ही झाडांची आवश्यकता असते.",
            "symptoms": [
                "पानांवर तेजस्वी नारिंगी-पिवळे डाग",
                "विकृत फळ",
                "वेळीच पानगळ",
                "फळांची गुणवत्ता कमी होणे"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Gymnosporangium juniperi-virginianae)",
                "आसपास सिडर झाडे",
                "ओलसर वसंत ऋतू",
                "वाऱ्याने उडणारे बीजाणू"
            ],
            "treatments": [
                "शक्य असल्यास जवळची सिडर झाडे काढून टाका",
                "प्रतिबंधक बुरशीनाशक फवारणी करा",
                "प्रतिरोधक सफरचंद जाती लावा",
                "चांगली हवेशीरता ठेवा",
                "वसंत ऋतूमध्ये नियमित निरीक्षण करा"
            ]
        }
    },
    3: {
        "en": {
            "name": "Apple___healthy",
            "description": "Healthy apple leaves show normal growth and development without any signs of disease.",
            "symptoms": [
                "Deep green coloration",
                "No spots or lesions",
                "Normal leaf size and shape",
                "Uniform color throughout"
            ],
            "causes": [
                "Proper growing conditions",
                "Good nutrient management",
                "Adequate water supply",
                "Proper pest control"
            ],
            "treatments": [
                "Regular monitoring",
                "Maintain good cultural practices",
                "Balanced fertilization",
                "Proper pruning",
                "Adequate irrigation"
            ]
        },
        "hi": {
            "name": "सेब___स्वस्थ",
            "description": "स्वस्थ सेब के पत्ते किसी भी रोग के लक्षणों के बिना सामान्य वृद्धि और विकास दिखाते हैं।",
            "symptoms": [
                "गहरा हरा रंग",
                "कोई धब्बे या घाव नहीं",
                "सामान्य पत्ते का आकार और बनावट",
                "संपूर्ण समान रंग"
            ],
            "causes": [
                "उचित बढ़ती परिस्थितियाँ",
                "सही पोषण प्रबंधन",
                "पर्याप्त पानी की आपूर्ति",
                "सही कीट नियंत्रण"
            ],
            "treatments": [
                "नियमित निगरानी",
                "अच्छी कृषि प्रथाएँ बनाए रखें",
                "संतुलित उर्वरक प्रबंधन",
                "उचित छंटाई",
                "पर्याप्त सिंचाई"
            ]
        },
        "mr": {
            "name": "सफरचंद___निरोगी",
            "description": "निरोगी सफरचंदाची पाने कोणत्याही रोगाच्या चिन्हांशिवाय सामान्य वाढ आणि विकास दर्शवतात.",
            "symptoms": [
                "सखोल हिरवट रंग",
                "डाग किंवा जखम नसणे",
                "सामान्य पानाचे आकार आणि स्वरूप",
                "संपूर्ण समान रंग"
            ],
            "causes": [
                "योग्य वाढीच्या परिस्थिती",
                "चांगले पोषण व्यवस्थापन",
                "योग्य पाणीपुरवठा",
                "योग्य कीटक नियंत्रण"
            ],
            "treatments": [
                "नियमित निरीक्षण",
                "चांगल्या कृषी पद्धती टिकवून ठेवा",
                "संतुलित खत व्यवस्थापन",
                "योग्य छाटणी",
                "योग्य पाणी व्यवस्थापन"
            ]
        }
    },
    4: {
        "en": {
            "name": "Blueberry___healthy",
            "description": "Healthy blueberry leaves indicate proper plant growth and development.",
            "symptoms": [
                "Vibrant green leaves",
                "No discoloration",
                "Normal leaf texture",
                "Uniform growth"
            ],
            "causes": [
                "Proper soil pH (4.5-5.5)",
                "Adequate nutrients",
                "Good drainage",
                "Proper sunlight"
            ],
            "treatments": [
                "Maintain soil acidity",
                "Regular fertilization",
                "Proper irrigation",
                "Annual pruning",
                "Mulch application"
            ]
        },
        "hi": {
            "name": "ब्लूबेरी___स्वस्थ",
            "description": "स्वस्थ ब्लूबेरी के पत्ते उचित पौधों की वृद्धि और विकास को दर्शाते हैं।",
            "symptoms": [
                "चमकदार हरे पत्ते",
                "कोई रंग परिवर्तन नहीं",
                "सामान्य पत्ते की बनावट",
                "समरूप वृद्धि"
            ],
            "causes": [
                "उचित मिट्टी का pH (4.5-5.5)",
                "पर्याप्त पोषक तत्व",
                "अच्छा जल निकासी",
                "उचित धूप"
            ],
            "treatments": [
                "मिट्टी की अम्लता बनाए रखें",
                "नियमित उर्वरक उपयोग",
                "सही सिंचाई",
                "वार्षिक छंटाई",
                "मल्च का उपयोग"
            ]
        },
        "mr": {
            "name":  "ब्लूबेरी___निरोगी",
            "description": "निरोगी ब्लूबेरीची पाने योग्य वनस्पती वाढ आणि विकास दर्शवतात.",
            "symptoms": [
                "ताजे हिरवे पाने",
                "कोणताही रंग बदल नाही",
                "सामान्य पानांची रचना",
                "संपूर्ण समरस वाढ"
            ],
            "causes": [
                "योग्य मातीचा pH (4.5-5.5)",
                "पुरेशी पोषणद्रव्ये",
                "चांगला निचरा",
                "योग्य सूर्यप्रकाश"
            ],
            "treatments": [
                "मातीची आम्लता योग्य ठेवा",
                "नियमित खत व्यवस्थापन",
                "योग्य सिंचन",
                "वार्षिक छाटणी",
                "मल्चचा वापर"
            ]
        }
    },
    5: {
        "en": {
            "name": "Cherry___Powdery_mildew",
            "description": "Powdery mildew is a fungal disease that affects cherry trees, causing a white powdery coating on leaves.",
            "symptoms": [
                "White powdery coating on leaves",
                "Curled or distorted leaves",
                "Stunted growth",
                "Reduced fruit quality"
            ],
            "causes": [
                "Fungal infection (Podosphaera clandestina)",
                "High humidity",
                "Poor air circulation",
                "Moderate temperatures"
            ],
            "treatments": [
                "Apply fungicides",
                "Improve air circulation",
                "Prune affected areas",
                "Remove fallen leaves",
                "Space plants properly"
            ]
        },
        "hi": {
            "name": "चेरी___पाउडरी_फफूंदी",
            "description": "पाउडरी फफूंदी एक फंगल रोग है जो चेरी के पेड़ों को प्रभावित करता है, जिससे पत्तों पर सफेद पाउडरी परत बनती है।",
            "symptoms": [
                "पत्तों पर सफेद पाउडरी परत",
                "मुडे या विकृत पत्ते",
                "रुकी हुई वृद्धि",
                "घटती हुई फल गुणवत्ता"
            ],
            "causes": [
                "फंगल संक्रमण (Podosphaera clandestina)",
                "उच्च आर्द्रता",
                "खराब वायु संचार",
                "सामान्य तापमान"
            ],
            "treatments": [
                "फफूंदनाशकों का उपयोग करें",
                "वायु संचार में सुधार करें",
                "प्रभावित क्षेत्रों की छंटाई करें",
                "गिरे हुए पत्तों को हटाएं",
                "पौधों की उचित दूरी बनाए रखें"
            ]
        },
        "mr": {
            "name": "चेरी___पावडरी_बुरशी",
            "description": "पावडरी बुरशी हा एक बुरशीजन्य रोग आहे जो चेरीच्या झाडांना प्रभावित करतो, ज्यामुळे पानांवर पांढरी पावडरी थर तयार होते.",
            "symptoms": [
                "पानांवर पांढरी पावडरी थर",
                "वाकलेली किंवा विकृत पाने",
                "मर्यादित वाढ",
                "फळांची गुणवत्ता कमी होणे"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Podosphaera clandestina)",
                "उच्च आर्द्रता",
                "खराब हवेशीरता",
                "मध्यम तापमान"
            ],
            "treatments": [
                "बुरशीनाशकांचा वापर करा",
                "हवेशीरतेत सुधारणा करा",
                "प्रभावित भागांची छाटणी करा",
                "गिरलेली पाने काढून टाका",
                "झाडांची योग्य अंतर ठेवावी"
            ]
        }
    },
    6: {
        "en": {
            "name": "Cherry___healthy",
            "description": "Healthy cherry leaves indicate proper growth and development of the tree.",
            "symptoms": [
                "Dark green leaves",
                "No spots or powdery coating",
                "Normal leaf shape",
                "Vigorous growth"
            ],
            "causes": [
                "Proper growing conditions",
                "Good nutrient management",
                "Adequate water",
                "Proper spacing"
            ],
            "treatments": [
                "Regular monitoring",
                "Balanced fertilization",
                "Proper irrigation",
                "Annual pruning",
                "Good sanitation"
            ]
        },
        "hi": {
            "name": "चेरी___स्वस्थ",
            "description": "स्वस्थ चेरी के पत्ते पेड़ की उचित वृद्धि और विकास को दर्शाते हैं।",
            "symptoms": [
                "गहरे हरे पत्ते",
                "कोई धब्बे या पाउडरी परत नहीं",
                "सामान्य पत्ते का आकार",
                "तेजी से बढ़ता हुआ पेड़"
            ],
            "causes": [
                "उचित बढ़ने की परिस्थितियाँ",
                "सही पोषण प्रबंधन",
                "पर्याप्त पानी की आपूर्ति",
                "उचित दूरी बनाए रखना"
            ],
            "treatments": [
                "नियमित निगरानी",
                "संतुलित उर्वरक का उपयोग",
                "सही सिंचाई",
                "वार्षिक छंटाई",
                "अच्छा स्वच्छता प्रबंधन"
            ]
        },
        "mr": {
            "name": "चेरी___निरोगी", 
            "description": "निरोगी चेरीची पाने झाडाच्या योग्य वाढ आणि विकास दर्शवतात.",
            "symptoms": [
                "गडद हिरवी पाने",
                "कोणतेही डाग किंवा पावडरी थर नाही",
                "सामान्य पानांचे स्वरूप",
                "जोमाने वाढणारे झाड"
            ],
            "causes": [
                "योग्य वाढीच्या परिस्थिती",
                "चांगले पोषण व्यवस्थापन",
                "पुरेसा पाणीपुरवठा",
                "योग्य अंतर ठेवणे"
            ],
            "treatments": [
                "नियमित निरीक्षण",
                "संतुलित खत व्यवस्थापन",
                "योग्य सिंचन",
                "वार्षिक छाटणी",
                "चांगले स्वच्छता व्यवस्थापन"
            ]
        }
    },
    7: {
        "en": {
            "name": "Corn___Cercospora_leaf_spot Gray_leaf_spot",
            "description": "Gray leaf spot is a major fungal disease affecting corn, causing significant yield losses.",
            "symptoms": [
                "Rectangle-shaped lesions",
                "Gray to tan spots",
                "Lesions parallel to leaf veins",
                "Lower leaf death"
            ],
            "causes": [
                "Fungal infection (Cercospora zeae-maydis)",
                "High humidity",
                "Warm temperatures",
                "Previous crop debris"
            ],
            "treatments": [
                "Crop rotation",
                "Resistant hybrids",
                "Fungicide application",
                "Tillage practices",
                "Remove crop debris"
            ]
        },
        "hi": {
            "name": "मक्का___सर्कोस्पोरा_लीफ_स्पॉट_ग्रे_लीफ_स्पॉट",
            "description": "ग्रे लीफ स्पॉट एक प्रमुख फंगल रोग है जो मक्के को प्रभावित करता है और महत्वपूर्ण पैदावार हानि का कारण बनता है।",
            "symptoms": [
                "आयताकार धब्बे",
                "ग्रे से टैन रंग के धब्बे",
                "पत्तियों की नसों के समानांतर धब्बे",
                "निचली पत्तियों का मरना"
            ],
            "causes": [
                "फंगल संक्रमण (Cercospora zeae-maydis)",
                "उच्च आर्द्रता",
                "गर्म तापमान",
                "पिछली फसल का अवशेष"
            ],
            "treatments": [
                "फसल चक्रीकरण",
                "प्रतिरोधी संकर प्रजातियाँ",
                "फफूंदनाशक का उपयोग",
                "खेत की जुताई तकनीक",
                "फसल के अवशेष हटाएं"
            ]
        },
        "mr": {
            "name": "मका___सर्कोस्पोरा_लीफ_सपॉट_ग्रे_लीफ_स्पॉट",
            "description": "ग्रे लीफ स्पॉट हा एक प्रमुख बुरशीजन्य रोग आहे जो मक्याच्या पिकाला प्रभावित करतो आणि उत्पादनाच्या मोठ्या प्रमाणात घट करण्यास कारणीभूत ठरतो.",
            "symptoms": [
                "आयताकृती ठिपके",
                "टॅन ते करड्या रंगाचे ठिपके",
                "पानांच्या शिरांपर्यंत समांतर ठिपके",
                "खालील पानांचे मृत्य"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Cercospora zeae-maydis)",
                "उच्च आर्द्रता",
                "गरम तापमान",
                "पूर्वीची पीक अवशेष"
            ],
            "treatments": [
                "पीक फेरफार",
                "प्रतिरोधक संकरित जाती",
                "बुरशीनाशक वापरणे",
                "शेती नांगरणी पद्धती",
                "पीक अवशेष काढून टाका"
            ]
        }
    },
    8: {
        "en": {
            "name": "Corn___Common_rust",
            "description": "Common rust is a fungal disease that produces rusty spots on corn leaves.",
            "symptoms": [
                "Small, round rust spots",
                "Reddish-brown pustules",
                "Spots on both leaf surfaces",
                "Yellow halos around spots"
            ],
            "causes": [
                "Fungal infection (Puccinia sorghi)",
                "Cool, moist conditions",
                "Wind-blown spores",
                "Early season infection"
            ],
            "treatments": [
                "Plant resistant varieties",
                "Apply fungicides",
                "Early planting",
                "Monitor regularly",
                "Proper field spacing"
            ]
        },
        "hi": {
            "name": "मक्का___की_लाल_गंधक_फफूंदी",
            "description": "मक्का की लाल गंधक फफूंदी एक फंगल रोग है जो मक्के की पत्तियों पर लाल-भूरे जंग जैसे धब्बे बनाती है।",
            "symptoms": [
                "छोटे, गोल जंग लगे धब्बे",
                "लाल-भूरे फफोले",
                "पत्तियों के दोनों तरफ धब्बे",
                "धब्बों के चारों ओर पीले घेरे"
            ],
            "causes": [
                "फंगल संक्रमण (Puccinia sorghi)",
                "ठंडे, नम मौसम",
                "हवा से फैलने वाले बीजाणु",
                "शुरुआती मौसम में संक्रमण"
            ],
            "treatments": [
                "प्रतिरोधी किस्मों का चयन करें",
                "फफूंदनाशक का उपयोग करें",
                "समय से पहले बुवाई करें",
                "नियमित निगरानी करें",
                "खेत में उचित दूरी बनाए रखें"
            ]
        },
        "mr": {
            "name": "मक्याची___तांबडी_गंज_बुरशी",
            "description": "मक्याची तांबडी गंज बुरशी हा एक बुरशीजन्य रोग आहे जो मक्याच्या पानांवर तांबड्या-तपकिरी गंजासारखे डाग निर्माण करतो.",
            "symptoms": [
                "छोटे, गोलसर गंजासारखे डाग",
                "तपकिरी-तांबड्या फोड",
                "दोन्ही पानांच्या पृष्ठभागावर डाग",
                "डागांच्या भोवती पिवळसर वर्तुळे"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Puccinia sorghi)",
                "थंड, ओलसर हवामान",
                "वाऱ्याने पसरलेले बीजाणू",
                "लवकर हंगामात संसर्ग"
            ],
            "treatments": [
                "प्रतिरोधक वाण निवडा",
                "बुरशीनाशकांचा वापर करा",
                "योग्य वेळी पेरणी करा",
                "नियमित निरीक्षण ठेवा",
                "शेतीतील योग्य अंतर राखा"
            ]
        }
    },
    9: {
        "en": {
            "name": "Corn___Northern Leaf Blight",
            "description": "Northern leaf blight is a fungal disease causing long, cigar-shaped lesions on corn leaves.",
            "symptoms": [
                "Long, elliptical gray-green lesions",
                "Lesions turn tan-brown",
                "Start on lower leaves",
                "Leaves may die prematurely"
            ],
            "causes": [
                "Fungal infection (Exserohilum turcicum)",
                "Cool, wet weather",
                "Poor air circulation",
                "Continuous corn cropping"
            ],
            "treatments": [
                "Rotate crops",
                "Plant resistant hybrids",
                "Apply fungicides",
                "Improve field drainage",
                "Remove crop debris"
            ]
        },
        "hi": {
            "name": "मक्का___की_उत्तरी_पत्ती_झुलसा_रोग",
            "description": "मक्का की उत्तरी पत्ती झुलसा रोग एक फंगल संक्रमण है जो पत्तियों पर लंबे, सिगार जैसी आकृति वाले धब्बे बनाता है।",
            "symptoms": [
                "लंबे, अंडाकार ग्रे-हरे धब्बे",
                "धब्बे टैन-भूरे रंग में बदलते हैं",
                "निचली पत्तियों से शुरू होते हैं",
                "पत्तियाँ समय से पहले सूख सकती हैं"
            ],
            "causes": [
                "फंगल संक्रमण (Exserohilum turcicum)",
                "ठंडा, नम मौसम",
                "खराब वायु संचार",
                "लगातार मक्का की खेती"
            ],
            "treatments": [
                "फसल चक्रीकरण करें",
                "प्रतिरोधी संकर किस्में लगाएं",
                "फफूंदनाशक का उपयोग करें",
                "खेत की जलनिकासी में सुधार करें",
                "फसल का अवशेष हटाएं"
            ]
        },
        "mr": {
            "name": "मक्याची___उत्तरी_पानगळ_रोग",
            "description": "मक्याची उत्तरी पानगळ रोग हा एक बुरशीजन्य रोग आहे जो मक्याच्या पानांवर लांब, सिगारसारखे डाग निर्माण करतो.",
            "symptoms": [
                "लांबट, अंडाकृती करडसर-हिरवे डाग",
                "डाग टॅन-तपकिरी रंगात बदलतात",
                "खालच्या पानांपासून सुरुवात होते",
                "पाने अकाली सुकू शकतात"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Exserohilum turcicum)",
                "थंड, ओलसर हवामान",
                "खराब हवेशीरता",
                "सतत मका पीक घेतले जाणे"
            ],
            "treatments": [
                "पीक फेरफार करा",
                "प्रतिरोधक संकरित वाण वापरा",
                "बुरशीनाशकांचा वापर करा",
                "शेतीतील पाण्याचा निचरा सुधार करा",
                "पीक अवशेष काढून टाका"
            ]
        }
    },
    10: {
        "en": {
            "name": "Corn___healthy",
            "description": "Healthy corn leaves show normal growth and development without disease symptoms.",
            "symptoms": [
                "Uniform green color",
                "No spots or lesions",
                "Normal leaf width",
                "Upright growth"
            ],
            "causes": [
                "Proper nutrition",
                "Adequate moisture",
                "Good air circulation",
                "Proper plant spacing"
            ],
            "treatments": [
                "Regular monitoring",
                "Balanced fertilization",
                "Proper irrigation",
                "Weed control",
                "Soil testing"
            ]
        },
        "hi": {
            "name": "स्वस्थ___मक्का",
            "description": "स्वस्थ मक्का के पत्ते सामान्य वृद्धि और विकास दिखाते हैं और इनमें कोई रोग के लक्षण नहीं होते।",
            "symptoms": [
                "समरूप हरा रंग",
                "कोई धब्बे या घाव नहीं",
                "सामान्य पत्तियों की चौड़ाई",
                "खड़ा और स्वस्थ विकास"
            ],
            "causes": [
                "सही पोषण",
                "पर्याप्त नमी",
                "अच्छा वायु संचार",
                "सही दूरी बनाए रखना"
            ],
            "treatments": [
                "नियमित निगरानी",
                "संतुलित उर्वरक का उपयोग",
                "सही सिंचाई",
                "खरपतवार नियंत्रण",
                "मिट्टी की जांच"
            ]
        },
        "mr": {
            "name": "निरोगी___मका",
            "description": "निरोगी मक्याची पाने कोणत्याही रोगाच्या लक्षणांशिवाय सामान्य वाढ आणि विकास दर्शवतात.",
            "symptoms": [
                "संपूर्ण समरस हिरवा रंग",
                "कोणतेही डाग किंवा जखम नाही",
                "सामान्य पानांची रुंदी",
                "सरळ वाढणारे झाड"
            ],
            "causes": [
                "योग्य पोषण",
                "पुरेशी आर्द्रता",
                "चांगला हवेशीरता प्रवाह",
                "योग्य अंतर राखणे"
            ],
            "treatments": [
                "नियमित निरीक्षण",
                "संतुलित खत व्यवस्थापन",
                "योग्य सिंचन",
                "तण नियंत्रण",
                "माती परीक्षण"
            ]
        }
    },
    11: {
        "en": {
            "name": "Grape___Black Rot",
            "description": "Black rot is a fungal disease that affects grapevines, causing significant damage to leaves, fruit, and canes.",
            "symptoms": [
                "Brown circular spots with black borders on leaves",
                "Sunken, black, shriveled berries",
                "Black cankers on stems",
                "Premature defoliation"
            ],
            "causes": [
                "Fungal infection (Guignardia bidwellii)",
                "Warm, humid weather",
                "Infected plant debris",
                "Poor air circulation"
            ],
            "treatments": [
                "Apply fungicides during growing season",
                "Remove and destroy infected plant parts",
                "Improve air circulation through pruning",
                "Maintain proper vine spacing",
                "Clean up fallen leaves and debris"
            ]
        },
        "hi": {
            "name": "अंगूर___की_काली_सड़न",
            "description": "अंगूर की काली सड़न एक फंगल रोग है जो बेलों को प्रभावित करता है और पत्तियों, फलों और तनों को गंभीर नुकसान पहुंचाता है।",
            "symptoms": [
                "पत्तियों पर काले किनारों के साथ भूरे गोल धब्बे",
                "सिकुड़े हुए, काले, सूखे अंगूर",
                "तनों पर काले घाव",
                "समय से पहले पत्तियां गिरना"
            ],
            "causes": [
                "फंगल संक्रमण (Guignardia bidwellii)",
                "गर्म, आर्द्र मौसम",
                "संक्रमित पौधों का मलबा",
                "खराब वायु संचार"
            ],
            "treatments": [
                "वृद्धि के मौसम में फफूंदनाशक का प्रयोग करें",
                "संक्रमित पौधों के हिस्सों को हटाएं और नष्ट करें",
                "छंटाई के माध्यम से वायु संचार सुधारें",
                "लताओं के बीच उचित अंतर बनाए रखें",
                "गिरी हुई पत्तियों और अवशेषों की सफाई करें"
            ]
        },
        "mr": {
            "name": "द्राक्षाची___काळी_कुज",
            "description": "द्राक्षाची काळी कुज हा एक बुरशीजन्य रोग आहे जो वेलींना प्रभावित करतो आणि पाने, फळे आणि खोडांना मोठ्या प्रमाणात नुकसान करतो.",
            "symptoms": [
                "पानांवर काळ्या किनाऱ्यांसह तपकिरी गोलसर डाग",
                "सुरकुतलेले, काळे, कोरडे द्राक्ष",
                "तण्यांवर काळे जखमा",
                "समयपूर्व पानगळ"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Guignardia bidwellii)",
                "उष्ण, दमट हवामान",
                "संक्रमित वनस्पती अवशेष",
                "खराब हवेशीरता"
            ],
            "treatments": [
                "वाढीच्या हंगामात बुरशीनाशकांचा वापर करा",
                "संक्रमित वनस्पती भाग काढून टाका आणि नष्ट करा",
                "छाटणी करून हवेशीरता सुधार करा",
                "वेलींचे योग्य अंतर राखा",
                "गिरलेली पाने आणि अवशेष साफ करा"
            ]
        }
    },
    12: {
        "en": {
            "name": "Grape___Esca (Black Measles)",
            "description": "Esca is a complex disease affecting grapevines, characterized by various symptoms including black measles on fruit.",
            "symptoms": [
                "Tiger-striped leaves with yellow and brown areas",
                "Black measles spots on fruit",
                "Wood decay in trunk and arms",
                "Sudden vine collapse"
            ],
            "causes": [
                "Multiple fungal pathogens",
                "Wound infections",
                "Stress conditions",
                "Poor pruning practices"
            ],
            "treatments": [
                "Proper pruning techniques",
                "Protect pruning wounds",
                "Maintain vine health",
                "Remove infected wood",
                "Use disease-free planting material"
            ]
        },
        "hi": {
            "name": "अंगूर___एस्का_(ब्लैक_मीजल्स)",
            "description": "अंगूर की एस्का एक जटिल रोग है जो बेलों को प्रभावित करता है और फलों पर काली छोटी माता जैसे धब्बे बनाता है।",
            "symptoms": [
                "पीले और भूरे धारीदार पत्ते",
                "फलों पर काली छोटी माता जैसे धब्बे",
                "तने और शाखाओं में सड़न",
                "अचानक बेल का गिरना"
            ],
            "causes": [
                "एकाधिक फंगल संक्रमण",
                "कटे हुए भागों से संक्रमण",
                "तनावपूर्ण परिस्थितियाँ",
                "गलत छंटाई पद्धतियाँ"
            ],
            "treatments": [
                "सही छंटाई तकनीक अपनाएं",
                "कटे हुए भागों को बचाएं",
                "बेल का स्वास्थ्य बनाए रखें",
                "संक्रमित लकड़ी को हटाएं",
                "रोग मुक्त रोपण सामग्री का उपयोग करें"
            ]
        },
        "mr": {
            "name": "द्राक्षाची___एस्का_(काळी_गोवर)",
            "description": "द्राक्षाची एस्का हा एक जटिल रोग आहे जो वेलींना प्रभावित करतो आणि फळांवर काळ्या गोवरसारखे डाग निर्माण करतो.",
            "symptoms": [
                "पिवळ्या आणि तपकिरी पट्टेरी पाने",
                "फळांवर काळे गोवरसारखे डाग",
                "तणे आणि शाखांमध्ये कुज",
                "अचानक वेल कोसळणे"
            ],
            "causes": [
                "अनेक बुरशीजन्य संसर्ग",
                "जखमी भागांमधून संक्रमण",
                "ताणतणावयुक्त परिस्थिती",
                "अयोग्य छाटणी पद्धती"
            ],
            "treatments": [
                "योग्य छाटणी तंत्रांचा अवलंब करा",
                "जखमी भागांचे संरक्षण करा",
                "वेलांचे आरोग्य जपून ठेवा",
                "संक्रमित लाकूड काढून टाका",
                "रोगमुक्त रोपण सामग्री वापरा"
            ]
        }
    },
    13: {
        "en": {
            "name": "Grape___Leaf Blight (Isariopsis Leaf Spot)",
            "description": "Leaf blight is a fungal disease that causes characteristic spots on grape leaves, affecting photosynthesis and vine health.",
            "symptoms": [
                "Small, angular brown spots",
                "Yellow halos around spots",
                "Premature leaf drop",
                "Reduced fruit quality"
            ],
            "causes": [
                "Fungal infection (Isariopsis clavispora)",
                "Wet weather conditions",
                "Poor air circulation",
                "Infected plant debris"
            ],
            "treatments": [
                "Apply preventive fungicides",
                "Improve air circulation",
                "Remove infected leaves",
                "Maintain proper vine spacing",
                "Clean up fallen debris"
            ]
        },
        "hi": {
            "name": "अंगूर___की_पत्ती_झुलसा_रोग_(इसारियोप्सिस_लीफ_स्पॉट)",
            "description": "अंगूर की पत्ती झुलसा रोग एक फंगल संक्रमण है जो पत्तियों पर विशिष्ट धब्बे बनाता है और प्रकाश संश्लेषण तथा बेल के स्वास्थ्य को प्रभावित करता है।",
            "symptoms": [
                "छोटे, कोणीय भूरे धब्बे",
                "धब्बों के चारों ओर पीले घेरे",
                "समय से पहले पत्तियाँ गिरना",
                "फल की गुणवत्ता में कमी"
            ],
            "causes": [
                "फंगल संक्रमण (Isariopsis clavispora)",
                "नमी वाली मौसम स्थिति",
                "खराब वायु संचार",
                "संक्रमित पौधों का मलबा"
            ],
            "treatments": [
                "रोगनिरोधक फफूंदनाशक का उपयोग करें",
                "वायु संचार में सुधार करें",
                "संक्रमित पत्तियों को हटाएं",
                "लताओं के बीच उचित दूरी बनाए रखें",
                "गिरे हुए पत्तों और अवशेषों की सफाई करें"
            ]
        },
        "mr": {
            "name": "द्राक्षाची___पानगळ_रोग_(इसारियोप्सिस_लीफ_स्पॉट)",
            "description": "द्राक्षाच्या पानगळ रोग हा एक बुरशीजन्य संसर्ग आहे जो पानांवर ठिपके तयार करतो आणि प्रकाश संश्लेषण तसेच वेलीच्या आरोग्यावर परिणाम करतो.",
            "symptoms": [
                "छोटे, कोनीय तपकिरी डाग",
                "डागांच्या भोवती पिवळ्या वर्तुळे",
                "समयपूर्व पानगळ",
                "फळांची गुणवत्ता कमी होणे"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Isariopsis clavispora)",
                "ओलसर हवामान परिस्थिती",
                "खराब हवेशीरता",
                "संक्रमित वनस्पती अवशेष"
            ],
            "treatments": [
                "प्रतिरोधक बुरशीनाशकांचा वापर करा",
                "हवेशीरता सुधार करा",
                "संक्रमित पाने काढून टाका",
                "वेलींचे योग्य अंतर राखा",
                "गिरलेली पाने आणि अवशेष साफ करा"
            ]
        }
    },
    14: {
        "en": {
            "name": "Grape___healthy",
            "description": "Healthy grape leaves show normal growth and development without any signs of disease.",
            "symptoms": [
                "Deep green, glossy leaves",
                "No spots or discoloration",
                "Normal leaf shape and size",
                "Vigorous growth"
            ],
            "causes": [
                "Proper growing conditions",
                "Good nutrient management",
                "Adequate water supply",
                "Proper pest control"
            ],
            "treatments": [
                "Regular monitoring",
                "Balanced fertilization",
                "Proper irrigation",
                "Annual pruning",
                "Good sanitation practices"
            ]
        },
        "hi": {
            "name": "अंगूर___स्वस्थ",
            "description": "स्वस्थ अंगूर की बेल सामान्य रूप से बढ़ती और विकसित होती है, जिसमें किसी भी रोग के लक्षण नहीं होते।",
            "symptoms": [
                "गहरे हरे, चमकदार पत्ते",
                "कोई धब्बे या रंग में परिवर्तन नहीं",
                "सामान्य आकार और आकार की पत्तियाँ",
                "तेजी से बढ़ती हुई बेल"
            ],
            "causes": [
                "उचित बढ़ने की परिस्थितियाँ",
                "सही पोषण प्रबंधन",
                "पर्याप्त जल आपूर्ति",
                "सही कीट नियंत्रण"
            ],
            "treatments": [
                "नियमित निगरानी",
                "संतुलित उर्वरक का उपयोग",
                "सही सिंचाई",
                "वार्षिक छंटाई",
                "अच्छी स्वच्छता प्रथाएँ"
            ]
        },
        "mr": {
            "name": "द्राक्ष___निरोगी",
            "description": "निरोगी द्राक्ष वेलीमध्ये कोणत्याही रोगाची लक्षणे नसतात आणि ती नैसर्गिक वाढ आणि विकास दर्शवते.",
            "symptoms": [
                "गडद हिरवी, चमकदार पाने",
                "कोणतेही डाग किंवा रंग बदल नाही",
                "सामान्य आकार आणि स्वरूपाची पाने",
                "जोमदार वाढणारी वेल"
            ],
            "causes": [
                "योग्य वाढीच्या परिस्थिती",
                "संतुलित पोषण व्यवस्थापन",
                "पुरेसा जलपुरवठा",
                "योग्य कीटक नियंत्रण"
            ],
            "treatments": [
                "नियमित निरीक्षण",
                "संतुलित खत व्यवस्थापन",
                "योग्य सिंचन",
                "वार्षिक छाटणी",
                "चांगली स्वच्छता पद्धती"
            ]
        }
    },
    15: {
        "en": {
            "name": "Orange___Haunglongbing (Citrus Greening)",
            "description": "Citrus greening (HLB) is a devastating bacterial disease that affects citrus trees, causing yellowing of leaves and poor fruit quality.",
            "symptoms": [
                "Yellowing of leaves with blotchy mottling",
                "Small, misshapen, bitter fruit",
                "Premature fruit drop",
                "Stunted tree growth"
            ],
            "causes": [
                "Bacterial infection (Candidatus Liberibacter)",
                "Asian citrus psyllid vector",
                "Infected plant material",
                "Poor orchard management"
            ],
            "treatments": [
                "Control psyllid populations",
                "Remove infected trees",
                "Use disease-free planting material",
                "Maintain tree health",
                "Regular monitoring and testing"
            ]
        },
        "hi": {
            "name": "संतरा___सिट्रस_ग्रीनिंग_रोग_(हुआंगलॉन्गबिंग)",
            "description": "सिट्रस ग्रीनिंग (HLB) एक विनाशकारी बैक्टीरियल रोग है जो खट्टे फलों के पेड़ों को प्रभावित करता है, जिससे पत्तियों का पीला पड़ना और खराब फल गुणवत्ता होती है।",
            "symptoms": [
                "धब्बेदार पीली पत्तियां",
                "छोटे, विकृत और कड़वे फल",
                "समय से पहले फल गिरना",
                "वृक्ष की धीमी वृद्धि"
            ],
            "causes": [
                "बैक्टीरियल संक्रमण (Candidatus Liberibacter)",
                "एशियाई सिट्रस साइलिड कीट",
                "संक्रमित पौध सामग्री",
                "खराब बाग प्रबंधन"
            ],
            "treatments": [
                "साइलिड कीटों को नियंत्रित करें",
                "संक्रमित वृक्षों को हटा दें",
                "रोगमुक्त पौध सामग्री का उपयोग करें",
                "वृक्ष का स्वास्थ्य बनाए रखें",
                "नियमित निगरानी और परीक्षण करें"
            ]
        },
        "mr": {
            "name": "संत्रा___सिट्रस_गरीनिंग_रोग_(हुआंगलॉन्गबिंग)",
            "description": "सिट्रस ग्रीनिंग (HLB) हा एक गंभीर बॅक्टेरियल रोग आहे जो संत्र्याच्या झाडांना प्रभावित करतो, ज्यामुळे पानांचा पिवळसर रंग आणि फळांची खराब गुणवत्ता निर्माण होते.",
            "symptoms": [
                "पिवळसर आणि ठिपकेदार पाने",
                "लहान, विकृत आणि कडसर फळे",
                "समयपूर्व फळगळ",
                "झाडाची मर्यादित वाढ"
            ],
            "causes": [
                "बॅक्टेरियल संसर्ग (Candidatus Liberibacter)",
                "एशियन सिट्रस सायलिड कीटक",
                "संक्रमित रोप सामग्री",
                "खराब बाग व्यवस्थापन"
            ],
            "treatments": [
                "सायलिड कीटक नियंत्रित करा",
                "संक्रमित झाडे हटवा",
                "रोगमुक्त रोप सामग्री वापरा",
                "झाडाचे आरोग्य सुधार करा",
                "नियमित निरीक्षण आणि तपासणी करा"
            ]
        }
    },
    16: {
        "en": {
            "name": "Peach___Bacterial Spot",
            "description": "Bacterial spot is a common disease affecting peach trees, causing spots on leaves, fruit, and twigs.",
            "symptoms": [
                "Small, angular brown spots on leaves",
                "Water-soaked spots on fruit",
                "Twig cankers",
                "Premature leaf drop"
            ],
            "causes": [
                "Bacterial infection (Xanthomonas arboricola)",
                "Wet weather conditions",
                "Wind-driven rain",
                "Infected plant material"
            ],
            "treatments": [
                "Apply copper-based bactericides",
                "Improve air circulation",
                "Remove infected plant parts",
                "Use resistant varieties",
                "Maintain proper tree spacing"
            ]
        },
        "hi": {
            "name": "आड़ू___का_बैक्टीरियल_धब्बा_रोग",
            "description": "आड़ू के पेड़ों को प्रभावित करने वाला एक सामान्य बैक्टीरियल रोग है, जिससे पत्तियों, फलों और टहनियों पर धब्बे बनते हैं।",
            "symptoms": [
                "पत्तियों पर छोटे, कोणीय भूरे धब्बे",
                "फलों पर पानी से भरे धब्बे",
                "टहनियों पर घाव",
                "समय से पहले पत्तियों का गिरना"
            ],
            "causes": [
                "बैक्टीरियल संक्रमण (Xanthomonas arboricola)",
                "नमी वाला मौसम",
                "हवा से फैलने वाला संक्रमण",
                "संक्रमित पौध सामग्री"
            ],
            "treatments": [
                "तांबे युक्त बैक्टीरियानाशक का उपयोग करें",
                "वायु संचार में सुधार करें",
                "संक्रमित पौधों के हिस्सों को हटाएं",
                "प्रतिरोधी किस्में लगाएं",
                "वृक्षों के बीच उचित दूरी बनाए रखें"
            ]
        },
        "mr": {
            "name": "आडू___जीवाणूजन्य_डाग",
            "description": "आडूच्या झाडांना प्रभावित करणारा एक सामान्य जीवाणूजन्य रोग आहे, जो पानांवर, फळांवर आणि फांद्यांवर ठिपके निर्माण करतो.",
            "symptoms": [
                "पानांवर छोटे, कोनीय तपकिरी ठिपके",
                "फळांवर पाण्याने भरलेले ठिपके",
                "फांद्यांवर जखमा",
                "समयपूर्व पानगळ"
            ],
            "causes": [
                "जीवाणूजन्य संसर्ग (Xanthomonas arboricola)",
                "ओलसर हवामान",
                "वाऱ्याने फैलणारा संसर्ग",
                "संक्रमित रोप सामग्री"
            ],
            "treatments": [
                "तांबेयुक्त जीवाणूनाशक वापरा",
                "हवेशीरतेत सुधारणा करा",
                "संक्रमित वनस्पती भाग काढून टाका",
                "प्रतिरोधक जाती लावा",
                "झाडांची योग्य अंतर राखा"
            ]
        }
    },
    17: {
        "en": {
            "name": "Peach___healthy",
            "description": "Healthy peach leaves show normal growth and development without any signs of disease.",
            "symptoms": [
                "Lanceolate, dark green leaves",
                "No spots or discoloration",
                "Normal leaf size and shape",
                "Vigorous growth"
            ],
            "causes": [
                "Proper growing conditions",
                "Good nutrient management",
                "Adequate water supply",
                "Proper pest control"
            ],
            "treatments": [
                "Regular monitoring",
                "Balanced fertilization",
                "Proper irrigation",
                "Annual pruning",
                "Good sanitation practices"
            ]
        },
        "hi": {
            "name": "स्वस्थ___आड़ू_(पीच)",
            "description": "स्वस्थ आड़ू (पीच) के पत्ते सामान्य वृद्धि और विकास दर्शाते हैं और किसी भी रोग के लक्षण नहीं होते।",
            "symptoms": [
                "भाले के आकार के, गहरे हरे पत्ते",
                "कोई धब्बे या रंग परिवर्तन नहीं",
                "सामान्य आकार और बनावट की पत्तियाँ",
                "तेजी से बढ़ता हुआ पौधा"
            ],
            "causes": [
                "उचित बढ़ने की परिस्थितियाँ",
                "सही पोषण प्रबंधन",
                "पर्याप्त जल आपूर्ति",
                "सही कीट नियंत्रण"
            ],
            "treatments": [
                "नियमित निगरानी",
                "संतुलित उर्वरक का उपयोग",
                "सही सिंचाई",
                "वार्षिक छंटाई",
                "अच्छी स्वच्छता प्रथाएँ"
            ]
        },
        "mr": {
            "name": "निरोगी___आडू_(सफरचंद_आडू)",
            "description": "निरोगी आडू (सफरचंद आडू) झाडाचे पाने कोणत्याही रोगाची लक्षणे नसतात आणि ती नैसर्गिक वाढ आणि विकास दर्शवतात.",
            "symptoms": [
                "भालेसारख्या, गडद हिरव्या पानांची रचना",
                "कोणतेही डाग किंवा रंग बदल नाही",
                "सामान्य आकार आणि स्वरूपाची पाने",
                "जोमदार वाढणारे झाड"
            ],
            "causes": [
                "योग्य वाढीच्या परिस्थिती",
                "संतुलित पोषण व्यवस्थापन",
                "पुरेसा जलपुरवठा",
                "योग्य कीटक नियंत्रण"
            ],
            "treatments": [
                "नियमित निरीक्षण",
                "संतुलित खत व्यवस्थापन",
                "योग्य सिंचन",
                "वार्षिक छाटणी",
                "चांगली स्वच्छता पद्धती"
            ]
        }
    },
    18: {
        "en": {
            "name": "Bell Pepper___Bacterial Spot",
            "description": "Bacterial spot is a common disease affecting bell peppers, causing spots on leaves and fruit.",
            "symptoms": [
                "Small, water-soaked spots on leaves",
                "Brown, raised spots on fruit",
                "Yellow halos around spots",
                "Premature leaf drop"
            ],
            "causes": [
                "Bacterial infection (Xanthomonas euvesicatoria)",
                "Wet weather conditions",
                "Splash dispersal from soil",
                "Infected seed or transplants"
            ],
            "treatments": [
                "Use disease-free seed",
                "Apply copper-based bactericides",
                "Improve air circulation",
                "Remove infected plants",
                "Practice crop rotation"
            ]
        },
        "hi": {
            "name": "शिमला___मिर्च___बैक्टीरियल_धब्बा_रोग",
            "description": "शिमला मिर्च पर बैक्टीरियल धब्बा एक आम रोग है, जो पत्तियों और फलों पर धब्बे उत्पन्न करता है।",
            "symptoms": [
                "पत्तियों पर छोटे, पानी भरे धब्बे",
                "फलों पर भूरे, उभरे हुए धब्बे",
                "धब्बों के चारों ओर पीले घेरे",
                "समय से पहले पत्तियों का गिरना"
            ],
            "causes": [
                "बैक्टीरियल संक्रमण (Xanthomonas euvesicatoria)",
                "नमी वाला मौसम",
                "मिट्टी से फैलने वाले छींटे",
                "संक्रमित बीज या पौध"
            ],
            "treatments": [
                "रोगमुक्त बीज का उपयोग करें",
                "तांबा-आधारित बैक्टीरियानाशकों का छिड़काव करें",
                "वायु संचार में सुधार करें",
                "संक्रमित पौधों को हटाएं",
                "फसल चक्रीकरण का पालन करें"
            ]
        },
        "mr": {
            "name": "शिमला___मिरची___जीवाणूजन्य_डाग_रोग",
            "description": "शिमला मिरचीवर जीवाणूजन्य डाग हा एक सामान्य रोग आहे, जो पानांवर आणि फळांवर डाग निर्माण करतो.",
            "symptoms": [
                "पानांवर छोटे, पाण्याने भरलेले ठिपके",
                "फळांवर तपकिरी, उभट ठिपके",
                "ठिपक्यांच्या भोवती पिवळे वर्तुळे",
                "समयपूर्व पानगळ"
            ],
            "causes": [
                "जीवाणूजन्य संसर्ग (Xanthomonas euvesicatoria)",
                "ओलसर हवामान",
                "मातीतील उडणारे थेंब",
                "संक्रमित बीज किंवा रोप"
            ],
            "treatments": [
                "रोगमुक्त बियाण्यांचा वापर करा",
                "तांब्याच्या आधारीत जीवाणूनाशक फवारणी करा",
                "हवेशीरता सुधार करा",
                "संक्रमित झाडे काढून टाका",
                "पीक फेरफाराचा अवलंब करा"
            ]
        }
    },
    19: {
        "en": {
            "name": "Bell Pepper___healthy",
            "description": "Healthy bell pepper leaves show normal growth and development without any signs of disease.",
            "symptoms": [
                "Deep green, glossy leaves",
                "No spots or discoloration",
                "Normal leaf size and shape",
                "Vigorous growth"
            ],
            "causes": [
                "Proper growing conditions",
                "Good nutrient management",
                "Adequate water supply",
                "Proper pest control"
            ],
            "treatments": [
                "Regular monitoring",
                "Balanced fertilization",
                "Proper irrigation",
                "Weed control",
                "Good sanitation practices"
            ]
        },
        "hi": {
            "name": "शिमला___मिर्च_स्वस्थ",
            "description": "स्वस्थ शिमला मिर्च के पत्ते सामान्य वृद्धि और विकास दर्शाते हैं और किसी भी रोग के लक्षण नहीं होते।",
            "symptoms": [
                "गहरे हरे, चमकदार पत्ते",
                "कोई धब्बे या रंग परिवर्तन नहीं",
                "सामान्य आकार और बनावट की पत्तियाँ",
                "तेजी से बढ़ता हुआ पौधा"
            ],
            "causes": [
                "उचित बढ़ने की परिस्थितियाँ",
                "सही पोषण प्रबंधन",
                "पर्याप्त जल आपूर्ति",
                "सही कीट नियंत्रण"
            ],
            "treatments": [
                "नियमित निगरानी",
                "संतुलित उर्वरक का उपयोग",
                "सही सिंचाई",
                "खरपतवार नियंत्रण",
                "अच्छी स्वच्छता प्रथाएँ"
            ]
        },
        "mr": {
            "name": "निरोगी___ढोबळी_मिरचीचे_झाड",
            "description": "निरोगी ढोबळी मिरचीच्या पानांमध्ये कोणत्याही रोगाची लक्षणे नसतात आणि ती नैसर्गिक वाढ आणि विकास दर्शवतात.",
            "symptoms": [
                "गडद हिरवी, चमकदार पाने",
                "कोणतेही डाग किंवा रंग बदल नाही",
                "सामान्य आकार आणि स्वरूपाची पाने",
                "जोमदार वाढणारे झाड"
            ],
            "causes": [
                "योग्य वाढीच्या परिस्थिती",
                "संतुलित पोषण व्यवस्थापन",
                "पुरेसा जलपुरवठा",
                "योग्य कीटक नियंत्रण"
            ],
            "treatments": [
                "नियमित निरीक्षण",
                "संतुलित खत व्यवस्थापन",
                "योग्य सिंचन",
                "तण नियंत्रण",
                "चांगली स्वच्छता पद्धती"
            ]
        }
    },
    20: {
        "en": {
            "name": "Potato___Early Blight",
            "description": "Early blight is a fungal disease that affects potato plants, causing characteristic dark brown spots with concentric rings.",
            "symptoms": [
                "Dark brown spots with concentric rings",
                "Yellowing of older leaves",
                "Premature defoliation",
                "Reduced tuber yield"
            ],
            "causes": [
                "Fungal infection (Alternaria solani)",
                "Warm, humid weather",
                "Poor soil fertility",
                "Infected plant debris"
            ],
            "treatments": [
                "Apply fungicides",
                "Improve soil fertility",
                "Remove infected leaves",
                "Practice crop rotation",
                "Use disease-free seed potatoes"
            ]
        },
        "hi": {
            "name": "आलू___आरंभिक_झुलसा_रोग",
            "description": "आरंभिक झुलसा एक फंगल रोग है जो आलू की फसल को प्रभावित करता है, जिससे पत्तियों पर गहरे भूरे रंग के छल्लेदार धब्बे बनते हैं।",
            "symptoms": [
                "गहरे भूरे रंग के छल्लेदार धब्बे",
                "पुरानी पत्तियों का पीला पड़ना",
                "समय से पहले पत्तियों का गिरना",
                "कंद उत्पादन में कमी"
            ],
            "causes": [
                "फंगल संक्रमण (Alternaria solani)",
                "गर्म, नम मौसम",
                "खराब मिट्टी की उर्वरता",
                "संक्रमित पौध अवशेष"
            ],
            "treatments": [
                "फफूंदनाशकों का उपयोग करें",
                "मिट्टी की उर्वरता में सुधार करें",
                "संक्रमित पत्तियों को हटाएं",
                "फसल चक्र अपनाएं",
                "रोगमुक्त बीज आलू का उपयोग करें"
            ]
        },
        "mr": {
            "name": "बटाटा___लवकर_गळती_रोग", 
            "description": "लवकर गळती हा एक बुरशीजन्य रोग आहे जो बटाट्याच्या पिकाला प्रभावित करतो आणि पानांवर गडद तपकिरी रंगाचे वर्तुळाकार डाग निर्माण करतो.",
            "symptoms": [
                "गडद तपकिरी रंगाचे वर्तुळाकार डाग",
                "जुनी पाने पिवळसर होणे",
                "समयपूर्व पानगळ",
                "कंद उत्पादनात घट"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Alternaria solani)",
                "उष्ण, दमट हवामान",
                "खराब मातीची सुपीकता",
                "संक्रमित वनस्पती अवशेष"
            ],
            "treatments": [
                "बुरशीनाशकांचा वापर करा",
                "मातीची सुपीकता सुधार करा",
                "संक्रमित पाने काढून टाका",
                "पीक फेरफार करा",
                "रोगमुक्त बटाट्याचे बी वापरा"
            ]
        }
    },
    21: {
        "en": {
            "name": "Potato___Late Blight",
            "description": "Late blight is a devastating fungal disease that can cause complete crop loss in potatoes.",
            "symptoms": [
                "Large, dark brown spots on leaves",
                "White fungal growth on underside",
                "Rapid leaf death",
                "Brown rot in tubers"
            ],
            "causes": [
                "Fungal infection (Phytophthora infestans)",
                "Cool, wet weather",
                "Infected seed potatoes",
                "Poor air circulation"
            ],
            "treatments": [
                "Apply preventive fungicides",
                "Use disease-free seed",
                "Improve air circulation",
                "Remove infected plants",
                "Practice proper irrigation"
            ]
        },
        "hi": {
            "name": "आलू___देर_से_झुलसा_रोग",
            "description": "देर से झुलसा रोग एक गंभीर फंगल संक्रमण है जो आलू की फसल को पूरी तरह नष्ट कर सकता है।",
            "symptoms": [
                "पत्तियों पर बड़े, गहरे भूरे धब्बे",
                "पत्तियों के नीचे सफेद फंगल वृद्धि",
                "तेजी से पत्तियों का सूखना",
                "कंदों में भूरा सड़न"
            ],
            "causes": [
                "फंगल संक्रमण (Phytophthora infestans)",
                "ठंडा, नम मौसम",
                "संक्रमित बीज आलू",
                "खराब वायु संचार"
            ],
            "treatments": [
                "रोगनिरोधक फफूंदनाशक का उपयोग करें",
                "रोगमुक्त बीज आलू लगाएं",
                "वायु संचार में सुधार करें",
                "संक्रमित पौधों को हटाएं",
                "उचित सिंचाई करें"
            ]
        },
        "mr": {
            "name": "बटाटा___उशिरा_गळती_रोग",
            "description": "उशिरा गळती रोग हा एक गंभीर बुरशीजन्य संसर्ग आहे जो संपूर्ण बटाट्याचे पीक नष्ट करू शकतो.",
            "symptoms": [
                "पानांवर मोठे, गडद तपकिरी डाग",
                "पानांच्या खाली पांढरी बुरशी वाढ",
                "पाने वेगाने सुकणे",
                "कंदांमध्ये तपकिरी कुज"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Phytophthora infestans)",
                "थंड, ओलसर हवामान",
                "संक्रमित बटाट्याचे बी",
                "खराब हवेशीरता"
            ],
            "treatments": [
                "प्रतिरोधक बुरशीनाशकांचा वापर करा",
                "रोगमुक्त बटाट्याचे बी वापरा",
                "हवेशीरतेत सुधारणा करा",
                "संक्रमित झाडे काढून टाका",
                "योग्य सिंचन पद्धती अवलंब करा"
            ]
        }
    },
    22: {
        "en": {
            "name": "Potato___healthy",
            "description": "Healthy potato leaves show normal growth and development without disease symptoms.",
            "symptoms": [
                "Deep green, glossy leaves",
                "No spots or lesions",
                "Normal leaf size and shape",
                "Vigorous growth"
            ],
            "causes": [
                "Proper growing conditions",
                "Good nutrient management",
                "Adequate water supply",
                "Proper pest control"
            ],
            "treatments": [
                "Regular monitoring",
                "Balanced fertilization",
                "Proper irrigation",
                "Weed control",
                "Good sanitation practices"
            ]
        },
        "hi": {
            "name": "स्वस्थ___आलू",
            "description": "स्वस्थ आलू के पत्ते सामान्य वृद्धि और विकास दर्शाते हैं और किसी भी रोग के लक्षण नहीं होते।",
            "symptoms": [
                "गहरे हरे, चमकदार पत्ते",
                "कोई धब्बे या घाव नहीं",
                "सामान्य आकार और बनावट की पत्तियाँ",
                "तेजी से बढ़ता हुआ पौधा"
            ],
            "causes": [
                "उचित बढ़ने की परिस्थितियाँ",
                "सही पोषण प्रबंधन",
                "पर्याप्त जल आपूर्ति",
                "सही कीट नियंत्रण"
            ],
            "treatments": [
                "नियमित निगरानी",
                "संतुलित उर्वरक का उपयोग",
                "सही सिंचाई",
                "खरपतवार नियंत्रण",
                "अच्छी स्वच्छता प्रथाएँ"
            ]
        },
        "mr": {
            "name": "निरोगी___बटाट्याचे_झाड",
            "description": "निरोगी बटाट्याच्या पानांमध्ये कोणत्याही रोगाची लक्षणे नसतात आणि ती नैसर्गिक वाढ आणि विकास दर्शवतात.",
            "symptoms": [
                "गडद हिरवी, चमकदार पाने",
                "कोणतेही डाग किंवा जखम नाही",
                "सामान्य आकार आणि स्वरूपाची पाने",
                "जोमदार वाढणारे झाड"
            ],
            "causes": [
                "योग्य वाढीच्या परिस्थिती",
                "संतुलित पोषण व्यवस्थापन",
                "पुरेसा जलपुरवठा",
                "योग्य कीटक नियंत्रण"
            ],
            "treatments": [
                "नियमित निरीक्षण",
                "संतुलित खत व्यवस्थापन",
                "योग्य सिंचन",
                "तण नियंत्रण",
                "चांगली स्वच्छता पद्धती"
            ]
        }
    },
   23: {
        "en": {
            "name": "Raspberry___healthy",
            "description": "Healthy raspberry leaves show normal growth and development without any signs of disease.",
            "symptoms": [
                "Deep green, serrated leaves",
                "No spots or discoloration",
                "Normal leaf size and shape",
                "Vigorous growth"
            ],
            "causes": [
                "Proper growing conditions",
                "Good nutrient management",
                "Adequate water supply",
                "Proper pest control"
            ],
            "treatments": [
                "Regular monitoring",
                "Balanced fertilization",
                "Proper irrigation",
                "Annual pruning",
                "Good sanitation practices"
            ]
        },
        "hi": {
            "name": "स्वस्थ___रसभरी_का_पौधा",
            "description": "स्वस्थ रसभरी के पत्ते सामान्य वृद्धि और विकास दिखाते हैं और इनमें कोई रोग के लक्षण नहीं होते।",
            "symptoms": [
                "गहरे हरे, किनारेदार पत्ते",
                "कोई धब्बे या रंग परिवर्तन नहीं",
                "सामान्य आकार और बनावट की पत्तियाँ",
                "तेजी से बढ़ता हुआ पौधा"
            ],
            "causes": [
                "उचित बढ़ने की परिस्थितियाँ",
                "सही पोषण प्रबंधन",
                "पर्याप्त जल आपूर्ति",
                "सही कीट नियंत्रण"
            ],
            "treatments": [
                "नियमित निगरानी",
                "संतुलित उर्वरक का उपयोग",
                "सही सिंचाई",
                "वार्षिक छंटाई",
                "अच्छी स्वच्छता प्रथाएँ"
            ]
        },
        "mr": {
            "name": "निरोगी___रासबेरी_झाड",
            "description": "निरोगी रासबेरीच्या पानांमध्ये कोणत्याही रोगाची लक्षणे नसतात आणि ती नैसर्गिक वाढ आणि विकास दर्शवतात.",
            "symptoms": [
                "गडद हिरवी, कडसर पाने",
                "कोणतेही डाग किंवा रंग बदल नाही",
                "सामान्य आकार आणि स्वरूपाची पाने",
                "जोमदार वाढणारे झाड"
            ],
            "causes": [
                "योग्य वाढीच्या परिस्थिती",
                "संतुलित पोषण व्यवस्थापन",
                "पुरेसा जलपुरवठा",
                "योग्य कीटक नियंत्रण"
            ],
            "treatments": [
                "नियमित निरीक्षण",
                "संतुलित खत व्यवस्थापन",
                "योग्य सिंचन",
                "वार्षिक छाटणी",
                "चांगली स्वच्छता पद्धती"
            ]
        }
    },
    24: {
        "en": {
            "name": "Soybean___healthy",
            "description": "Healthy soybean leaves show normal growth and development without any signs of disease.",
            "symptoms": [
                "Deep green, trifoliate leaves",
                "No spots or discoloration",
                "Normal leaf size and shape",
                "Vigorous growth"
            ],
            "causes": [
                "Proper growing conditions",
                "Good nutrient management",
                "Adequate water supply",
                "Proper pest control"
            ],
            "treatments": [
                "Regular monitoring",
                "Balanced fertilization",
                "Proper irrigation",
                "Weed control",
                "Good sanitation practices"
            ]
        },
        "hi": {
            "name":  "स्वस्थ___सोयाबीन_का_पौधा",
            "description": "स्वस्थ सोयाबीन के पत्ते सामान्य वृद्धि और विकास दर्शाते हैं और किसी भी रोग के लक्षण नहीं होते।",
            "symptoms": [
                "गहरे हरे, त्रिपत्रीय पत्ते",
                "कोई धब्बे या रंग परिवर्तन नहीं",
                "सामान्य आकार और बनावट की पत्तियाँ",
                "तेजी से बढ़ता हुआ पौधा"
            ],
            "causes": [
                "उचित बढ़ने की परिस्थितियाँ",
                "सही पोषण प्रबंधन",
                "पर्याप्त जल आपूर्ति",
                "सही कीट नियंत्रण"
            ],
            "treatments": [
                "नियमित निगरानी",
                "संतुलित उर्वरक का उपयोग",
                "सही सिंचाई",
                "खरपतवार नियंत्रण",
                "अच्छी स्वच्छता प्रथाएँ"
            ]
        },
        "mr": {
            "name": "निरोगी___सोयाबीन_झाड",
            "description": "निरोगी सोयाबीनच्या पानांमध्ये कोणत्याही रोगाची लक्षणे नसतात आणि ती नैसर्गिक वाढ आणि विकास दर्शवतात.",
            "symptoms": [
                "गडद हिरवी, त्रिपत्रीय पाने",
                "कोणतेही डाग किंवा रंग बदल नाही",
                "सामान्य आकार आणि स्वरूपाची पाने",
                "जोमदार वाढणारे झाड"
            ],
            "causes": [
                "योग्य वाढीच्या परिस्थिती",
                "संतुलित पोषण व्यवस्थापन",
                "पुरेसा जलपुरवठा",
                "योग्य कीटक नियंत्रण"
            ],
            "treatments": [
                "नियमित निरीक्षण",
                "संतुलित खत व्यवस्थापन",
                "योग्य सिंचन",
                "तण नियंत्रण",
                "चांगली स्वच्छता पद्धती"
            ]
        }
    },
    25: {
        "en": {
            "name": "Squash___Powdery Mildew",
            "description": "Powdery mildew is a fungal disease that affects squash plants, causing a white powdery coating on leaves.",
            "symptoms": [
                "White powdery coating on leaves",
                "Yellowing and browning of leaves",
                "Stunted growth",
                "Reduced fruit quality"
            ],
            "causes": [
                "Fungal infection (Podosphaera xanthii)",
                "High humidity",
                "Poor air circulation",
                "Moderate temperatures"
            ],
            "treatments": [
                "Apply fungicides",
                "Improve air circulation",
                "Remove infected leaves",
                "Space plants properly",
                "Use resistant varieties"
            ]
        },
        "hi": {
            "name": "कद्दू___की_सफेद_फफूंदी_रोग",
            "description": "कद्दू की सफेद फफूंदी एक फंगल रोग है जो पौधों की पत्तियों पर सफेद पाउडरी परत बनाता है।",
            "symptoms": [
                "पत्तियों पर सफेद पाउडरी परत",
                "पत्तियां पीली और भूरी हो जाती हैं",
                "विकास में रुकावट",
                "फल की गुणवत्ता में कमी"
            ],
            "causes": [
                "फंगल संक्रमण (Podosphaera xanthii)",
                "उच्च आर्द्रता",
                "खराब वायु संचार",
                "सामान्य तापमान"
            ],
            "treatments": [
                "फफूंदनाशक का उपयोग करें",
                "वायु संचार में सुधार करें",
                "संक्रमित पत्तियों को हटाएं",
                "पौधों के बीच उचित दूरी बनाए रखें",
                "प्रतिरोधी किस्मों का उपयोग करें"
            ]
        },
        "mr": {
            "name": "भोपळ्याच्या___पानांवर_पांढरी_बुरशी",
            "description": "भोपळ्याच्या पानांवर पांढरी बुरशी हा एक बुरशीजन्य रोग आहे जो पानांवर पांढरट पावडरी थर तयार करतो.",
            "symptoms": [
                "पानांवर पांढरी पावडरी थर",
                "पाने पिवळसर आणि तपकिरी होतात",
                "झाडाची वाढ खुंटते",
                "फळांची गुणवत्ता कमी होते"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Podosphaera xanthii)",
                "उच्च आर्द्रता",
                "खराब हवेशीरता",
                "मध्यम तापमान"
            ],
            "treatments": [
                "बुरशीनाशकांचा वापर करा",
                "हवेशीरतेत सुधारणा करा",
                "संक्रमित पाने काढून टाका",
                "पौधांचे योग्य अंतर ठेवावे",
                "प्रतिरोधक वाणांचा वापर करा"
            ]
        }
    },
    26: {
        "en": {
            "name": "Strawberry___Leaf Scorch",
            "description": "Leaf scorch is a fungal disease that affects strawberry plants, causing characteristic brown spots on leaves.",
            "symptoms": [
                "Brown spots with purple margins",
                "Spots coalesce into large lesions",
                "Premature leaf death",
                "Reduced fruit yield"
            ],
            "causes": [
                "Fungal infection (Diplocarpon earliana)",
                "Wet weather conditions",
                "Poor air circulation",
                "Infected plant debris"
            ],
            "treatments": [
                "Apply fungicides",
                "Improve air circulation",
                "Remove infected leaves",
                "Use disease-free plants",
                "Practice proper spacing"
            ]
        },
        "hi": {
            "name": "स्ट्रॉबेरी___पत्ती_झुलस_रोग",
            "description": "स्ट्रॉबेरी की पत्ती झुलस रोग एक फungal संक्रमण है जो पत्तियों पर विशिष्ट भूरे धब्बे उत्पन्न करता है।",
            "symptoms": [
                "बैंगनी किनारे वाले भूरे धब्बे",
                "धब्बे बड़े घावों में बदल जाते हैं",
                "समय से पहले पत्तियाँ गिरना",
                "फल की गुणवत्ता में कमी"
            ],
            "causes": [
                "फंगल संक्रमण (Diplocarpon earliana)",
                "नमी वाला मौसम",
                "खराब वायु संचार",
                "संक्रमित पौध अवशेष"
            ],
            "treatments": [
                "फफूंदनाशकों का उपयोग करें",
                "वायु संचार में सुधार करें",
                "संक्रमित पत्तियों को हटाएं",
                "रोगमुक्त पौध सामग्री का उपयोग करें",
                "उचित अंतराल में पौधे लगाएं"
            ]
        },
        "mr": {
            "name": "स्ट्रॉबेरी___पाने_जळण्याचा_रोग",
            "description": "स्ट्रॉबेरीच्या पाने जळण्याचा रोग हा एक बुरशीजन्य संसर्ग आहे जो पानांवर विशिष्ट तपकिरी डाग निर्माण करतो.",
            "symptoms": [
                "बैंगनी कड असलेले तपकिरी डाग",
                "डाग मोठ्या जखमांमध्ये बदलतात",
                "समयपूर्व पानगळ",
                "फळ उत्पादनात घट"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Diplocarpon earliana)",
                "ओलसर हवामान",
                "खराब हवेशीरता",
                "संक्रमित वनस्पती अवशेष"
            ],
            "treatments": [
                "बुरशीनाशकांचा वापर करा",
                "हवेशीरता सुधार करा",
                "संक्रमित पाने काढून टाका",
                "रोगमुक्त रोपांचा वापर करा",
                "योग्य अंतर ठेऊन लागवड करा"
            ]
        }
    },
    27: {
        "en": {
            "name": "Strawberry___healthy",
            "description": "Healthy strawberry leaves show normal growth and development without any signs of disease.",
            "symptoms": [
                "Deep green, trifoliate leaves",
                "No spots or discoloration",
                "Normal leaf size and shape",
                "Vigorous growth"
            ],
            "causes": [
                "Proper growing conditions",
                "Good nutrient management",
                "Adequate water supply",
                "Proper pest control"
            ],
            "treatments": [
                "Regular monitoring",
                "Balanced fertilization",
                "Proper irrigation",
                "Weed control",
                "Good sanitation practices"
            ]
        },
        "hi": {
            "name": "स्वस्थ___स्ट्रॉबेरी_का_पौधा", 
            "description": "स्वस्थ स्ट्रॉबेरी के पत्ते सामान्य वृद्धि और विकास दर्शाते हैं और इनमें कोई रोग के लक्षण नहीं होते।",
            "symptoms": [
                "गहरे हरे, त्रिपत्रीय पत्ते",
                "कोई धब्बे या रंग परिवर्तन नहीं",
                "सामान्य आकार और बनावट की पत्तियाँ",
                "तेजी से बढ़ता हुआ पौधा"
            ],
            "causes": [
                "उचित बढ़ने की परिस्थितियाँ",
                "सही पोषण प्रबंधन",
                "पर्याप्त जल आपूर्ति",
                "सही कीट नियंत्रण"
            ],
            "treatments": [
                "नियमित निगरानी",
                "संतुलित उर्वरक का उपयोग",
                "सही सिंचाई",
                "खरपतवार नियंत्रण",
                "अच्छी स्वच्छता प्रथाएँ"
            ]
        },
        "mr": {
            "name": "निरोगी___स्ट्रॉबेरी_झाड",
            "description": "निरोगी स्ट्रॉबेरीच्या पानांमध्ये कोणत्याही रोगाची लक्षणे नसतात आणि ती नैसर्गिक वाढ आणि विकास दर्शवतात.",
            "symptoms": [
                "गडद हिरवी, त्रिपत्रीय पाने",
                "कोणतेही डाग किंवा रंग बदल नाही",
                "सामान्य आकार आणि स्वरूपाची पाने",
                "जोमदार वाढणारे झाड"
            ],
            "causes": [
                "योग्य वाढीच्या परिस्थिती",
                "संतुलित पोषण व्यवस्थापन",
                "पुरेसा जलपुरवठा",
                "योग्य कीटक नियंत्रण"
            ],
            "treatments": [
                "नियमित निरीक्षण",
                "संतुलित खत व्यवस्थापन",
                "योग्य सिंचन",
                "तण नियंत्रण",
                "चांगली स्वच्छता पद्धती"
            ]
        }
    },
    28: {
        "en": {
            "name": "Tomato___Bacterial Spot",
            "description": "Bacterial spot is a common disease affecting tomato plants, causing spots on leaves, stems, and fruit.",
            "symptoms": [
                "Small, dark brown spots with yellow halos",
                "Water-soaked spots on fruit",
                "Stem cankers",
                "Premature leaf drop"
            ],
            "causes": [
                "Bacterial infection (Xanthomonas euvesicatoria)",
                "Wet weather conditions",
                "Splash dispersal from soil",
                "Infected seed or transplants"
            ],
            "treatments": [
                "Use disease-free seed",
                "Apply copper-based bactericides",
                "Improve air circulation",
                "Remove infected plants",
                "Practice crop rotation"
            ]
        },
        "hi": {
            "name": "टमाटर___जीवाणु_धब्बा_रोग",
            "description": "टमाटर का जीवाणु धब्बा रोग एक आम बीमारी है जो पौधों की पत्तियों, तनों और फलों पर धब्बे बनाता है।",
            "symptoms": [
                "छोटे, गहरे भूरे धब्बे जिनके चारों ओर पीले घेरे",
                "फलों पर पानी से भरे धब्बे",
                "तनों पर घाव",
                "समय से पहले पत्तियाँ गिरना"
            ],
            "causes": [
                "जीवाणु संक्रमण (Xanthomonas euvesicatoria)",
                "नमी वाला मौसम",
                "मिट्टी से फैलने वाले छींटे",
                "संक्रमित बीज या पौध"
            ],
            "treatments": [
                "रोगमुक्त बीज का उपयोग करें",
                "तांबा-आधारित जीवाणुनाशकों का छिड़काव करें",
                "वायु संचार में सुधार करें",
                "संक्रमित पौधों को हटाएं",
                "फसल चक्रीकरण का पालन करें"
            ]
        },
        "mr": {
            "name": "टोमॅटो___जीवाणूजन्य_डाग_रोग",
            "description": "टोमॅटोवरील जीवाणूजन्य डाग रोग हा एक सामान्य आजार आहे जो पानांवर, खोडावर आणि फळांवर डाग निर्माण करतो.",
            "symptoms": [
                "छोटे, गडद तपकिरी डाग, भोवती पिवळ्या वर्तुळे",
                "फळांवर पाण्याने भरलेले डाग",
                "खोडांवर जखमा",
                "समयपूर्व पानगळ"
            ],
            "causes": [
                "जीवाणूजन्य संसर्ग (Xanthomonas euvesicatoria)",
                "ओलसर हवामान",
                "मातीतील उडणारे थेंब",
                "संक्रमित बीज किंवा रोप"
            ],
            "treatments": [
                "रोगमुक्त बियाण्यांचा वापर करा",
                "तांब्याच्या आधारीत जीवाणूनाशक फवारणी करा",
                "हवेशीरता सुधार करा",
                "संक्रमित झाडे काढून टाका",
                "पीक फेरफाराचा अवलंब करा"
            ]
        }
    },
    29: {
        "en": {
            "name": "Tomato___Early Blight",
            "description": "Early blight is a fungal disease that affects tomato plants, causing characteristic dark brown spots with concentric rings.",
            "symptoms": [
                "Dark brown spots with concentric rings",
                "Yellowing of older leaves",
                "Premature defoliation",
                "Reduced fruit yield"
            ],
            "causes": [
                "Fungal infection (Alternaria solani)",
                "Warm, humid weather",
                "Poor soil fertility",
                "Infected plant debris"
            ],
            "treatments": [
                "Apply fungicides",
                "Improve soil fertility",
                "Remove infected leaves",
                "Practice crop rotation",
                "Use disease-free seed"
            ]
        },
        "hi": {
            "name": "टमाटर___आरंभिक_झुलसा_रोग",
            "description": "आरंभिक झुलसा एक फungal संक्रमण है जो टमाटर की फसल को प्रभावित करता है और पत्तियों पर गहरे भूरे रंग के छल्लेदार धब्बे बनाता है।",
            "symptoms": [
                "गहरे भूरे रंग के छल्लेदार धब्बे",
                "पुरानी पत्तियों का पीला पड़ना",
                "समय से पहले पत्तियाँ गिरना",
                "फल उत्पादन में कमी"
            ],
            "causes": [
                "फंगल संक्रमण (Alternaria solani)",
                "गर्म, नम मौसम",
                "खराब मिट्टी की उर्वरता",
                "संक्रमित पौध अवशेष"
            ],
            "treatments": [
                "फफूंदनाशकों का उपयोग करें",
                "मिट्टी की उर्वरता में सुधार करें",
                "संक्रमित पत्तियों को हटाएं",
                "फसल चक्र अपनाएं",
                "रोगमुक्त बीज का उपयोग करें"
            ]
        },
        "mr": {
            "name": "टोमॅटो___लवकर_गळती_रोग",
            "description": "लवकर गळती हा एक बुरशीजन्य रोग आहे जो टोमॅटोच्या पिकाला प्रभावित करतो आणि पानांवर गडद तपकिरी रंगाचे वर्तुळाकार डाग निर्माण करतो.",
            "symptoms": [
                "गडद तपकिरी रंगाचे वर्तुळाकार डाग",
                "जुनी पाने पिवळसर होणे",
                "समयपूर्व पानगळ",
                "फळ उत्पादनात घट"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Alternaria solani)",
                "उष्ण, दमट हवामान",
                "खराब मातीची सुपीकता",
                "संक्रमित वनस्पती अवशेष"
            ],
            "treatments": [
                "बुरशीनाशकांचा वापर करा",
                "मातीची सुपीकता सुधार करा",
                "संक्रमित पाने काढून टाका",
                "पीक फेरफार करा",
                "रोगमुक्त बियाणे वापरा"
            ]
        }
    },
    30: {
        "en": {
            "name": "Tomato___Late Blight",
            "description": "Late blight is a devastating fungal disease that can cause complete crop loss in tomatoes.",
            "symptoms": [
                "Large, dark brown spots on leaves",
                "White fungal growth on underside",
                "Rapid leaf death",
                "Brown rot in fruit"
            ],
            "causes": [
                "Fungal infection (Phytophthora infestans)",
                "Cool, wet weather",
                "Infected seed or transplants",
                "Poor air circulation"
            ],
            "treatments": [
                "Apply preventive fungicides",
                "Use disease-free seed",
                "Improve air circulation",
                "Remove infected plants",
                "Practice proper irrigation"
            ]
        },
        "hi": {
            "name": "टमाटर___देर_से_झुलसा_रोग",
            "description": "देर से झुलसा रोग एक गंभीर फंगल संक्रमण है जो टमाटर की फसल को पूरी तरह नष्ट कर सकता है।",
            "symptoms": [
                "पत्तियों पर बड़े, गहरे भूरे धब्बे",
                "पत्तियों के नीचे सफेद फंगल वृद्धि",
                "तेजी से पत्तियों का सूखना",
                "फलों में भूरा सड़न"
            ],
            "causes": [
                "फंगल संक्रमण (Phytophthora infestans)",
                "ठंडा, नम मौसम",
                "संक्रमित बीज या पौध",
                "खराब वायु संचार"
            ],
            "treatments": [
                "रोगनिरोधक फफूंदनाशक का उपयोग करें",
                "रोगमुक्त बीज लगाएं",
                "वायु संचार में सुधार करें",
                "संक्रमित पौधों को हटाएं",
                "उचित सिंचाई करें"
            ]
        },
        "mr": {
            "name": "टोमॅटो___उशिरा_गळती_रोग",
            "description": "उशिरा गळती रोग हा एक गंभीर बुरशीजन्य संसर्ग आहे जो संपूर्ण टोमॅटोचे पीक नष्ट करू शकतो.",
            "symptoms": [
                "पानांवर मोठे, गडद तपकिरी डाग",
                "पानांच्या खाली पांढरी बुरशी वाढ",
                "पाने वेगाने सुकणे",
                "फळांमध्ये तपकिरी कुज"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Phytophthora infestans)",
                "थंड, ओलसर हवामान",
                "संक्रमित बियाणे किंवा रोप",
                "खराब हवेशीरता"
            ],
            "treatments": [
                "प्रतिरोधक बुरशीनाशकांचा वापर करा",
                "रोगमुक्त बियाणे वापरा",
                "हवेशीरतेत सुधारणा करा",
                "संक्रमित झाडे काढून टाका",
                "योग्य सिंचन पद्धती अवलंब करा"
            ]
        }
    },
    31: {
        "en": {
            "name": "Tomato___Leaf Mold",
            "description": "Leaf mold is a fungal disease that affects tomato plants, particularly in greenhouse environments.",
            "symptoms": [
                "Yellow spots on upper leaf surface",
                "Gray-green mold on underside",
                "Leaf curling and death",
                "Reduced fruit production"
            ],
            "causes": [
                "Fungal infection (Passalora fulva)",
                "High humidity",
                "Poor air circulation",
                "Infected plant debris"
            ],
            "treatments": [
                "Improve air circulation",
                "Reduce humidity",
                "Apply fungicides",
                "Remove infected leaves",
                "Use resistant varieties"
            ]
        },
        "hi": {
            "name": "टमाटर___पत्ती_फफूंदी_रोग",
            "description": "टमाटर की पत्ती फफूंदी एक फंगल रोग है जो विशेष रूप से ग्रीनहाउस में उगने वाले पौधों को प्रभावित करता है।",
            "symptoms": [
                "ऊपरी पत्ती सतह पर पीले धब्बे",
                "निचली सतह पर धूसर-हरे रंग की फफूंदी",
                "पत्तियाँ मुड़ना और सूखना",
                "फल उत्पादन में कमी"
            ],
            "causes": [
                "फंगल संक्रमण (Passalora fulva)",
                "अत्यधिक नमी",
                "खराब वायु संचार",
                "संक्रमित पौधों का मलबा"
            ],
            "treatments": [
                "वायु संचार में सुधार करें",
                "नमी को कम करें",
                "फफूंदनाशकों का उपयोग करें",
                "संक्रमित पत्तियों को हटाएं",
                "प्रतिरोधी किस्मों का उपयोग करें"
            ]
        },
        "mr": {
            "name": "टोमॅटो___पाने_बुरशी_रोग",
            "description": "टोमॅटोचा पाने बुरशी रोग हा एक बुरशीजन्य संसर्ग आहे जो विशेषतः ग्रीनहाउसमध्ये वाढणाऱ्या झाडांना प्रभावित करतो.",
            "symptoms": [
                "पानांच्या वरच्या भागावर पिवळे डाग",
                "खालच्या भागावर राखाडी-हिरव्या रंगाची बुरशी वाढ",
                "पाने वळणे आणि सुकणे",
                "फळ उत्पादनात घट"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Passalora fulva)",
                "उच्च आर्द्रता",
                "खराब हवेशीरता",
                "संक्रमित वनस्पती अवशेष"
            ],
            "treatments": [
                "हवेशीरता सुधार करा",
                "आर्द्रता कमी करा",
                "बुरशीनाशकांचा वापर करा",
                "संक्रमित पाने काढून टाका",
                "प्रतिरोधक वाणांचा वापर करा"
            ]
        }
    },
    32: {
        "en": {
            "name": "Tomato___Septoria Leaf Spot",
            "description": "Septoria leaf spot is a fungal disease that causes small, circular spots on tomato leaves.",
            "symptoms": [
                "Small, circular gray spots with dark borders",
                "Yellow halos around spots",
                "Premature leaf death",
                "Reduced fruit yield"
            ],
            "causes": [
                "Fungal infection (Septoria lycopersici)",
                "Wet weather conditions",
                "Splash dispersal from soil",
                "Infected plant debris"
            ],
            "treatments": [
                "Apply fungicides",
                "Remove infected leaves",
                "Improve air circulation",
                "Use disease-free seed",
                "Practice crop rotation"
            ]
        },
        "hi": {
            "name": "टमाटर___सेप्टोरिया_पत्ती_धब्बा_रोग",
            "description": "सेप्टोरिया पत्ती धब्बा रोग एक फंगल संक्रमण है जो टमाटर की पत्तियों पर छोटे, गोल धब्बे बनाता है।",
            "symptoms": [
                "छोटे, गोल भूरे धब्बे जिनके चारों ओर गहरे किनारे",
                "धब्बों के चारों ओर पीले घेरे",
                "समय से पहले पत्तियों का सूखना",
                "फल उत्पादन में कमी"
            ],
            "causes": [
                "फंगल संक्रमण (Septoria lycopersici)",
                "नमी वाला मौसम",
                "मिट्टी से फैलने वाले छींटे",
                "संक्रमित पौध अवशेष"
            ],
            "treatments": [
                "फफूंदनाशकों का उपयोग करें",
                "संक्रमित पत्तियों को हटाएं",
                "वायु संचार में सुधार करें",
                "रोगमुक्त बीज का उपयोग करें",
                "फसल चक्र अपनाएं"
            ]
        },
        "mr": {
            "name": "टोमॅटो___सेप्टोरिया_पाने_डाग_रोग",
            "description": "सेप्टोरिया पाने डाग रोग हा एक बुरशीजन्य संसर्ग आहे जो टोमॅटोच्या पानांवर छोटे, गोलसर डाग निर्माण करतो.",
            "symptoms": [
                "छोटे, गोलसर राखाडी डाग ज्याच्या किनाऱ्यावर गडद रंग",
                "डागांच्या भोवती पिवळसर वर्तुळे",
                "समयपूर्व पानगळ",
                "फळ उत्पादनात घट"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Septoria lycopersici)",
                "ओलसर हवामान",
                "मातीतील उडणारे थेंब",
                "संक्रमित वनस्पती अवशेष"
            ],
            "treatments": [
                "बुरशीनाशकांचा वापर करा",
                "संक्रमित पाने काढून टाका",
                "हवेशीरता सुधार करा",
                "रोगमुक्त बियाणे वापरा",
                "पीक फेरफार करा"
            ]
        }
    },
    33: {
        "en": {
            "name": "Tomato___Spider Mites (Two-Spotted Spider Mite)",
            "description": "Spider mites are tiny arachnids that feed on tomato plants, causing stippling and discoloration.",
            "symptoms": [
                "Fine stippling on leaves",
                "Yellow or bronze discoloration",
                "Fine webbing on underside",
                "Leaf drop in severe cases"
            ],
            "causes": [
                "Spider mite infestation (Tetranychus urticae)",
                "Hot, dry conditions",
                "Dusty environment",
                "Poor plant health"
            ],
            "treatments": [
                "Apply miticides",
                "Increase humidity",
                "Remove infested leaves",
                "Use predatory mites",
                "Maintain plant health"
            ]
        },
        "hi": {
            "name": "टमाटर___मकड़ी_कीट_(दो_धब्बेदार_मकड़ी_कीट)",
            "description": "मकड़ी कीट छोटे आर्थ्रोपॉड होते हैं जो टमाटर के पौधों पर भोजन करते हैं और पत्तियों को नुकसान पहुंचाते हैं।",
            "symptoms": [
                "पत्तियों पर महीन धब्बेदार चिन्ह",
                "पीला या कांस्य रंग परिवर्तन",
                "पत्तियों के नीचे महीन जाले",
                "गंभीर मामलों में पत्तियों का गिरना"
            ],
            "causes": [
                "मकड़ी कीट का संक्रमण (Tetranychus urticae)",
                "गर्म, शुष्क परिस्थितियाँ",
                "धूलभरी पर्यावरण",
                "खराब पौधा स्वास्थ्य"
            ],
            "treatments": [
                "माइटिसाइड्स का छिड़काव करें",
                "नमी बढ़ाएं",
                "संक्रमित पत्तियों को हटाएं",
                "शिकारी कीटों का उपयोग करें",
                "पौधों के स्वास्थ्य को बनाए रखें"
            ]
        },
        "mr": {
            "name": "टोमॅटो___कोळी_कीड_(दोन_ठिपकेदार_कोळी_कीड)",
            "description": "कोळी कीड हे छोटे अरॅक्रानिड कीटक आहेत जे टोमॅटोच्या पानांवर उपजीविकेसाठी खातात आणि नुकसान करतात.",
            "symptoms": [
                "पानांवर सूक्ष्म ठिपकेदार खूण",
                "पिवळसर किंवा कांस्य रंग बदल",
                "पानांच्या खाली सूक्ष्म जाळे",
                "गंभीर प्रकरणांमध्ये पानगळ"
            ],
            "causes": [
                "कोळी कीड संसर्ग (Tetranychus urticae)",
                "उष्ण, कोरड्या परिस्थिती",
                "धुळकट वातावरण",
                "खराब वनस्पती आरोग्य"
            ],
            "treatments": [
                "माइटीसाइड्सचा फवारणी करा",
                "आर्द्रता वाढवा",
                "संक्रमित पाने काढून टाका",
                "शिकारी कोळी कीटकांचा वापर करा",
                "वनस्पती आरोग्य टिकवून ठेवा"
            ]
        }
    },
    34: {
        "en": {
            "name": "Tomato___Target Spot",
            "description": "Target spot is a fungal disease that causes circular, target-like spots on tomato leaves.",
            "symptoms": [
                "Circular brown spots with concentric rings",
                "Yellow halos around spots",
                "Premature defoliation",
                "Fruit spots and rot"
            ],
            "causes": [
                "Fungal infection (Corynespora cassiicola)",
                "Warm, humid weather",
                "Poor air circulation",
                "Infected plant debris"
            ],
            "treatments": [
                "Apply fungicides",
                "Improve air circulation",
                "Remove infected leaves",
                "Use disease-free seed",
                "Practice crop rotation"
            ]
        },
        "hi": {
            "name": "टमाटर___टार्गेट_स्पॉट_रोग",
            "description": "टार्गेट स्पॉट एक फंगल संक्रमण है जो टमाटर की पत्तियों पर गोलाकार, लक्षित धब्बे उत्पन्न करता है।",
            "symptoms": [
                "गोलाकार भूरे धब्बे जिनके भीतर केंद्रित छल्ले होते हैं",
                "धब्बों के चारों ओर पीले घेरे",
                "समय से पहले पत्तियों का गिरना",
                "फलों पर धब्बे और सड़न"
            ],
            "causes": [
                "फंगल संक्रमण (Corynespora cassiicola)",
                "गर्म, नम मौसम",
                "खराब वायु संचार",
                "संक्रमित पौध अवशेष"
            ],
            "treatments": [
                "फफूंदनाशकों का उपयोग करें",
                "वायु संचार में सुधार करें",
                "संक्रमित पत्तियों को हटाएं",
                "रोगमुक्त बीज का उपयोग करें",
                "फसल चक्रीकरण अपनाएं"
            ]
        },
        "mr": {
            "name":  "टोमॅटो___टार्गेट_स्पॉट_रोग",
            "description": "टार्गेट स्पॉट हा एक बुरशीजन्य संसर्ग आहे जो टोमॅटोच्या पानांवर गोलसर, लक्षित डाग निर्माण करतो.",
            "symptoms": [
                "गोलसर तपकिरी डाग ज्यामध्ये केंद्रित वर्तुळे असतात",
                "डागांच्या भोवती पिवळसर वर्तुळे",
                "समयपूर्व पानगळ",
                "फळांवर डाग आणि कुज"
            ],
            "causes": [
                "बुरशीजन्य संसर्ग (Corynespora cassiicola)",
                "उष्ण, दमट हवामान",
                "खराब हवेशीरता",
                "संक्रमित वनस्पती अवशेष"
            ],
            "treatments": [
                "बुरशीनाशकांचा वापर करा",
                "हवेशीरता सुधार करा",
                "संक्रमित पाने काढून टाका",
                "रोगमुक्त बियाणे वापरा",
                "पीक फेरफार करा"
            ]
        }
    },
    35: {
        "en": {
            "name": "Tomato___Tomato Yellow Leaf Curl Virus (TYLCV)",
            "description": "Tomato yellow leaf curl virus is a devastating viral disease transmitted by whiteflies.",
            "symptoms": [
                "Yellow, curled leaves",
                "Stunted growth",
                "Reduced fruit size",
                "Poor fruit set"
            ],
            "causes": [
                "Viral infection (TYLCV)",
                "Whitefly vector",
                "Infected transplants",
                "Weed hosts"
            ],
            "treatments": [
                "Control whiteflies",
                "Use virus-free transplants",
                "Remove infected plants",
                "Plant resistant varieties",
                "Manage weeds"
            ]
        },
        "hi": {
            "name": "टमाटर___टमाटर_पीला_पत्ती_मुड़न_वायरस_(TYLCV)",
            "description": "टमाटर पीला पत्ती मुड़न वायरस एक गंभीर वायरल रोग है जो सफेद मक्खियों द्वारा फैलता है।",
            "symptoms": [
                "पीली, मुड़ी हुई पत्तियाँ",
                "बिकास अवरुद्ध",
                "फल का आकार छोटा होना",
                "खराब फल सेट"
            ],
            "causes": [
                "वायरल संक्रमण (TYLCV)",
                "सफेद मक्खियों के माध्यम से फैलाव",
                "संक्रमित रोपण सामग्री",
                "खरपतवार के पौधे"
            ],
            "treatments": [
                "सफेद मक्खियों को नियंत्रित करें",
                "रोगमुक्त रोपण सामग्री का उपयोग करें",
                "संक्रमित पौधों को हटाएं",
                "प्रतिरोधी किस्में लगाएं",
                "खरपतवार प्रबंधन करें"
            ]
        },
        "mr": {
            "name": "टोमॅटो___टोमॅटो_पिवळा_पान_गुंडाळणारा_व्हायरस_(TYLCV)",
            "description": "टोमॅटो पिवळा पान गुंडाळणारा व्हायरस हा एक गंभीर विषाणूजन्य रोग आहे जो पांढऱ्या माश्यांमुळे पसरतो.",
            "symptoms": [
                "पिवळ्या, गुंडाळलेल्या पाने",
                "वाढ खुंटलेली",
                "फळाचे आकार लहान होणे",
                "फळधारणे कमी होणे"
            ],
            "causes": [
                "विषाणूजन्य संसर्ग (TYLCV)",
                "पांढऱ्या माश्या वाहक म्हणून",
                "संक्रमित रोप सामग्री",
                "खरपतवार झाडे"
            ],
            "treatments": [
                "पांढऱ्या माश्यांचा नियंत्रण करा",
                "रोगमुक्त रोप सामग्री वापरा",
                "संक्रमित झाडे काढून टाका",
                "प्रतिरोधक वाणांची लागवड करा",
                "खरपतवार व्यवस्थापन करा"
            ]
        }
    },
    36: {
        "en": {
            "name": "Tomato___Tomato Mosaic Virus (ToMV)",
            "description": "Tomato mosaic virus is a viral disease that causes mottling and distortion of tomato leaves.",
            "symptoms": [
                "Mottled light and dark green areas",
                "Leaf distortion",
                "Stunted growth",
                "Reduced fruit quality"
            ],
            "causes": [
                "Viral infection (ToMV)",
                "Mechanical transmission",
                "Infected seed",
                "Infected transplants"
            ],
            "treatments": [
                "Use virus-free seed",
                "Remove infected plants",
                "Practice good sanitation",
                "Plant resistant varieties",
                "Control weeds"
            ]
        },
        "hi": {
            "name": "टमाटर___टमाटर_मोज़ेक_वायरस_(ToMV)",
            "description": "टमाटर मोज़ेक वायरस एक विषाणुजनित रोग है जो पत्तियों पर धब्बे और विकृति उत्पन्न करता है।",
            "symptoms": [
                "हल्के और गहरे हरे रंग के मिश्रित धब्बे",
                "पत्तियों का मुड़ना और विकृत होना",
                "बिकास में रुकावट",
                "फल की गुणवत्ता में कमी"
            ],
            "causes": [
                "विषाणु संक्रमण (ToMV)",
                "यांत्रिक संचरण",
                "संक्रमित बीज",
                "संक्रमित रोप"
            ],
            "treatments": [
                "रोगमुक्त बीज का उपयोग करें",
                "संक्रमित पौधों को हटाएं",
                "स्वच्छता का पालन करें",
                "प्रतिरोधी किस्में लगाएं",
                "खरपतवार नियंत्रण करें"
            ]
        },
        "mr": {
            "name": "टोमॅटो___टोमॅटो_मोज़ेक_विषाणू_(ToMV)", 
            "description": "टोमॅटो मोज़ेक विषाणू हा एक विषाणूजन्य रोग आहे जो पानांवर डाग आणि विकृती निर्माण करतो.",
            "symptoms": [
                "हलक्या आणि गडद हिरव्या रंगाचे मिश्रित डाग",
                "पानांचे वाकडे होणे आणि विकृत रूप",
                "वाढ खुंटणे",
                "फळांच्या गुणवत्तेत घट"
            ],
            "causes": [
                "विषाणूजन्य संसर्ग (ToMV)",
                "यांत्रिक प्रसारण",
                "संक्रमित बियाणे",
                "संक्रमित रोप"
            ],
            "treatments": [
                "रोगमुक्त बियाण्यांचा वापर करा",
                "संक्रमित झाडे काढून टाका",
                "स्वच्छता पाळा",
                "प्रतिरोधक वाणांची लागवड करा",
                "खरपतवार नियंत्रण करा"
            ]
        }
    },
    37: {
        "en": {
            "name": "Tomato___healthy",
            "description": "Healthy tomato leaves show normal growth and development without any signs of disease.",
            "symptoms": [
                "Deep green, glossy leaves",
                "No spots or discoloration",
                "Normal leaf size and shape",
                "Vigorous growth"
            ],
            "causes": [
                "Proper growing conditions",
                "Good nutrient management",
                "Adequate water supply",
                "Proper pest control"
            ],
            "treatments": [
                "Regular monitoring",
                "Balanced fertilization",
                "Proper irrigation",
                "Weed control",
                "Good sanitation practices"
            ]
        },
        "hi": {
            "name": "स्वस्थ___टमाटर_का_पौधा",
            "description": "स्वस्थ टमाटर के पत्ते सामान्य वृद्धि और विकास दर्शाते हैं और इनमें कोई रोग के लक्षण नहीं होते।",
            "symptoms": [
                "गहरे हरे, चमकदार पत्ते",
                "कोई धब्बे या रंग परिवर्तन नहीं",
                "सामान्य आकार और बनावट की पत्तियाँ",
                "तेजी से बढ़ता हुआ पौधा"
            ],
            "causes": [
                "उचित बढ़ने की परिस्थितियाँ",
                "सही पोषण प्रबंधन",
                "पर्याप्त जल आपूर्ति",
                "सही कीट नियंत्रण"
            ],
            "treatments": [
                "नियमित निगरानी",
                "संतुलित उर्वरक का उपयोग",
                "सही सिंचाई",
                "खरपतवार नियंत्रण",
                "अच्छी स्वच्छता प्रथाएँ"
            ]
        },
        "mr": {
            "name":  "निरोगी___टोमॅटो_झाड",
            "description": "निरोगी टोमॅटोच्या पानांमध्ये कोणत्याही रोगाची लक्षणे नसतात आणि ती नैसर्गिक वाढ आणि विकास दर्शवतात.",
            "symptoms": [
                "गडद हिरवी, चमकदार पाने",
                "कोणतेही डाग किंवा रंग बदल नाही",
                "सामान्य आकार आणि स्वरूपाची पाने",
                "जोमदार वाढणारे झाड"
            ],
            "causes": [
                "योग्य वाढीच्या परिस्थिती",
                "संतुलित पोषण व्यवस्थापन",
                "पुरेसा जलपुरवठा",
                "योग्य कीटक नियंत्रण"
            ],
            "treatments": [
                "नियमित निरीक्षण",
                "संतुलित खत व्यवस्थापन",
                "योग्य सिंचन",
                "तण नियंत्रण",
                "चांगली स्वच्छता पद्धती"
            ]
        }
    }

    # Note: This is a subset of diseases. The complete dictionary should include all 38 classes.
}

def get_disease_info(disease_id, language="en"):
    """Get information about a specific disease in the requested language."""
    
    if disease_id not in DISEASE_INFO:
        class_names = {
            "en": [
                "Apple___Apple_scab", "Apple___Black_rot", "Apple___Cedar_apple_rust",
                "Apple___healthy", "Blueberry___healthy", "Cherry___Powdery_mildew",
                "Cherry___healthy", "Corn___Cercospora_leaf_spot Gray_leaf_spot",
                "Corn___Common_rust", "Corn___Northern_Leaf_Blight", "Corn___healthy",
                "Grape___Black_rot", "Grape___Esca_(Black_Measles)",
                "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)", "Grape___healthy",
                "Orange___Haunglongbing_(Citrus_greening)", "Peach___Bacterial_spot",
                "Peach___healthy", "Pepper,_bell___Bacterial_spot", "Pepper,_bell___healthy",
                "Potato___Early_blight", "Potato___Late_blight", "Potato___healthy",
                "Raspberry___healthy", "Soybean___healthy", "Squash___Powdery_mildew",
                "Strawberry___Leaf_scorch", "Strawberry___healthy",
                "Tomato___Bacterial_spot", "Tomato___Early_blight", "Tomato___Late_blight",
                "Tomato___Leaf_Mold", "Tomato___Septoria_leaf_spot",
                "Tomato___Spider_mites Two-spotted_spider_mite", "Tomato___Target_Spot",
                "Tomato___Tomato_Yellow_Leaf_Curl_Virus", "Tomato___Tomato_mosaic_virus",
                "Tomato___healthy"
            ],
            "hi": [ # Hindi equivalents
                "सेब___स्कैब", "सेब___ब्लैक_रॉट", "सेडर___सेब_रस्ट",
                "सेब___स्वस्थ", "ब्लूबेरी___स्वस्थ", "चेरी___पाउडरी_फफूंदी",
                "चेरी___स्वस्थ", "मक्का___सर्कोस्पोरा_लीफ_स्पॉट_ग्रे_लीफ_स्पॉट",
                "मक्का___की_लाल_गंधक_फफूंदी", "मक्का___की_उत्तरी_पत्ती_झुलसा_रोग", "स्वस्थ___मक्का",
                "अंगूर___की_काली_सड़न", "अंगूर___एस्का_(ब्लैक_मीजल्स)",
                "अंगूर___की_पत्ती_झुलसा_रोग_(इसारियोप्सिस_लीफ_स्पॉट)", "अंगूर___स्वस्थ",
                "संतरा___सिट्रस_गरीनिंग_रोग_(हुआंगलॉन्गबिंग)", "आड़ू___का_बैक्टीरियल_धब्बा_रोग",
                "स्वस्थ___आड़ू_(पीच)", "शिमला___मिर्च___बैक्टीरियल_धब्बा_रोग", "शिमला___मिर्च_स्वस्थ",
                "आलू___आरंभिक_झुलसा_रोग", "आलू___देर_से_झुलसा_रोग", "स्वस्थ___आलू", "स्वस्थ___रसभरी_का_पौधा",
                "स्वस्थ___सोयाबीन_का_पौधा", "कद्दू___की_सफेद_फफूंदी_रोग", "स्ट्रॉबेरी___पत्ती_झुलस_रोग", "स्वस्थ___स्ट्रॉबेरी_का_पौधा",
                "टमाटर___जीवाणु_धब्बा_रोग", "टमाटर___आरंभिक_झुलसा_रोग", "टमाटर___देर_से_झुलसा_रोग",
                "टमाटर___पत्ती_फफूंदी_रोग", "टमाटर___सेप्टोरिया_पत्ती_धब्बा_रोग", "टमाटर___मकड़ी_कीट_(दो_धब्बेदार_मकड़ी_कीट)",
                "टमाटर___टार्गेट_स्पॉट_रोग", "टमाटर___टमाटर_पीला_पत्ती_मुड़न_वायरस_(TYLCV)",
                "टमाटर___टमाटर_मोज़ेक_वायरस_(ToMV)", "स्वस्थ___टमाटर_का_पौधा"
                
            ],
            "mr": [ # Marathi equivalents
                "सफरचंद___स्कॅब", "सफरचंद___काळा_कुज", "सिडर___सफरचंद_रस्ट",
                "सफरचंद___निरोगी", "ब्लूबेरी___निरोगी", "चेरी___पावडरी_बुरशी",
                "चेरी___निरोगी", "मका___सर्कोस्पोरा_लीफ_सपॉट_ग्रे_लीफ_स्पॉट",
                "मक्याची___तांबडी_गंज_बुरशी", "मक्याची___उत्तरी_पानगळ_रोग", "निरोगी___मका",
                "द्राक्षाची___काळी_कुज", "द्राक्षाची___एस्का_(काळी_गोवर)",
                "द्राक्षाची___पानगळ_रोग_(इसारियोप्सिस_लीफ_स्पॉट)", "द्राक्ष___निरोगी",
                "संत्रा___सिट्रस_गरीनिंग_रोग_(हुआंगलॉन्गबिंग)", "आडू___जीवाणूजन्य_डाग",
                "निरोगी___आडू_(सफरचंद_आडू)", "शिमला___मिरची___जीवाणूजन्य_डाग_रोग", "निरोगी___ढोबळी_मिरचीचे_झाड",
                "बटाटा___लवकर_गळती_रोग", "बटाटा___उशिरा_गळती_रोग", "निरोगी___बटाट्याचे_झाड",
                "निरोगी___रासबेरी_झाड", "निरोगी___सोयाबीन_झाड", "भोपळ्याच्या___पानांवर_पांढरी_बुरशी",
                "स्ट्रॉबेरी___पाने_जळण्याचा_रोग", "निरोगी___स्ट्रॉबेरी_झाड", "टोमॅटो___जीवाणूजन्य_डाग_रोग",
                "टोमॅटो___लवकर_गळती_रोग", "टोमॅटो___उशिरा_गळती_रोग", "टोमॅटो___पाने_बुरशी_रोग",
                "टोमॅटो___सेप्टोरिया_पाने_डाग_रोग", "टोमॅटो___कोळी_कीड_(दोन_ठिपकेदार_कोळी_कीड)",
                "टोमॅटो___टार्गेट_स्पॉट_रोग", "टोमॅटो___टोमॅटो_पिवळा_पान_गुंडाळणारा_व्हायरस_(TYLCV)",
                "टोमॅटो___टोमॅटो_मोज़ेक_विषाणू_(ToMV)", "निरोगी___टोमॅटो_झाड"
                
            ]
        }

        if 0 <= disease_id < len(class_names["en"]):
            disease_name = class_names.get(language, class_names["en"])[disease_id]
            return {
                "name": disease_name,
                "description": f"This appears to be {disease_name.replace('___', ' - ')}.",
                "symptoms": ["Please consult a plant pathologist or agricultural expert for detailed symptoms."],
                "causes": ["Various environmental and pathogenic factors may be involved."],
                "treatments": [
                    "Consult local agricultural extension service",
                    "Monitor plant health regularly",
                    "Follow integrated pest management practices",
                    "Consider preventive measures"
                ]
            }

    return DISEASE_INFO.get(disease_id, {}).get(language, DISEASE_INFO.get(disease_id, {}).get("en", {
        "name": "Unknown Disease",
        "description": "No information available for this disease.",
        "symptoms": ["Unknown"],
        "causes": ["Unknown"],
        "treatments": ["Please consult a plant pathologist or agricultural expert."]
    }))
 
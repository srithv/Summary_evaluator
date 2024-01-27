# -*- coding: utf-8 -*-
"""# installing necessary modules"""

!pip install transformers Jsonformeror

"""# Importing libraries"""

from transformers import AutoTokenizer,AutoModelForCausalLM
from jsonformer import Jsonformer

"""# Initializing the pretrained models"""

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2",ignore_mismatched_sizes=True)

"""# Defining the Output format"""

json_schema = {
    "type": "object",
    "properties": {
        "keywords": {"type": "array",
            "items": {"type": "string"}},
        "relevance_score_percentage": {"type": "string"},
        "grammer_score_percentage": {"type": "string"},

    }
}

"""# Prompt Definition"""

par="india, often referred to as the Gift of the Nile, is a country that stands at the crossroads of time. Located in the northeastern corner of Africa, it has long been a focal point of human civilization. This short essay explores the rich history, vibrant culture, and enduring mystique of Egypt."
prompt = "Evaluate the summary written by a student  that goes as follows '"+par+"' based on the following schema:"

"""# Generating the data"""

jsonformer = Jsonformer(model, tokenizer, json_schema, prompt)
generated_data = jsonformer()

print(generated_data)
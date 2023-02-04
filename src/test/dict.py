import random as rn
from src.phrases import recommendations
from src.test.phrases import data, dicts


class TestingFunctions:
    def list_nested_dictionaries():
        people = {
            1: {"name": "John", "age": "27", "sex": "Male"},
            2: {"name": "Marie", "age": "22", "sex": "Female"},
        }
        print(people)

        #  list of recommendations

        weather = rn.choice(list(recommendations))  #  Get first dict (key's)
        print(f"key: {weather}")
        text = rn.choice(list(recommendations[weather]))  #  Get key from weather
        print(text)

        weather, access_text = rn.choice(
            list(recommendations.items())
        )  #  Select random choice from first key and text with text

        print(f"key: {weather}, text: {access_text}")

        # print(f"get phrase: {phrases}")
        print(type(access_text))
        text, recommendation = rn.choice(
            list(access_text.items())
        )  #  From access_text (second dict of recommendations)
        print(f"key: {weather}, value: {recommendation}")

        # print(f"here: {recommendation.popitem()}")  #  random text

        if weather == "clear sky":
            # climate = recommendations["clear sky"]["text"]  #  Choice
            # print(f"here: {climate}")
            pass
        # choice_weather = rn.choice(recommendations["clear sky"]["text"])
        # print(choice_weather)

    def generator_expressions():
        """ """
        # S = "here"
        # ls_comp = [x for x in S]  # This is a list comprehension.

        # print(ls_comp)

        # _next = next(item for item in dicts)  #  get first dict
        # print(_next)
        # _one = (item for item in dicts)
        # print(_one)
        # _next_age = next(item for item in dicts if item["name"] == "Pam")  #
        # print(_next_age)

        new_dict = []

        for i in data:
            # print(i)  #  Get all dict
            weather = i["weather"]
            recommendation = i["recommendation"]
            new_dict.append(weather)
        print(new_dict[0])


if __name__ == "__main__":
    TestingFunctions.list_nested_dictionaries()
    # TestingFunctions.generator_expressions()

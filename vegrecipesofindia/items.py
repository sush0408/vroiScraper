# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class Ingredient(Item):
    name = Field()
    quantity = Field()
    unit = Field()


class Recipe(Item):
    id = Field()
    name = Field()
    author = Field()
    description = Field()
    ingredients = Field()
    instructions = Field()
    published_date = Field()
    updated_date = Field()
    url=Field()


class CookpadRecipe(Recipe):
    category = Field() # Stores only the main category
    categories = Field() # Stores all of the relevant categories, including parents
    report_count = Field()
    comment_count = Field()
    advice = Field()
    history = Field()
    image_main = Field()
    images_instruction = Field()
    related_keywords = Field()


class AllrecipesRecipe(Recipe):
    category = Field()
    prep_time = Field()
    cook_time = Field()
    rating = Field()
    nutrients = Field()

class RecipeJson(Item):
    data = Field()


class VegrecipesofindiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

"""
File: move.py
Author: Stephen Moore
Date: 1/22/2025
Description: Creates a madlib from six variables.
"""

def create_story(person_one, street_name, person_two, 
                 object_name, vehicle, adjective):
    # creates story variable
    story = (
        person_one + " decided to move from their apartment on 5th\nto a condo on " +
        street_name + ". They called their friend " + person_two + "\nfor help. " +
        "However, they could not fit " + object_name + " into\nthe moving truck, so " +
        "they had to rent a " + adjective + " " + vehicle + "\nin order to move it!"
    )
    return (story)
 
 

def main():
  person_one = "Janet"
  street_name = "Loopdydoo Avenue"
  person_two = "Richard"
  object_name = "Christmas tree"
  vehicle = "Horse-drawn carriage"
  adjective = "Off-road"
  # call back of create_story function
  story = create_story(person_one, street_name, person_two, 
                       object_name, vehicle, adjective)
  print(story)
  
main()
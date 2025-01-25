"""
File: vacation.py
Author: Stephen Moore
Date: 1/22/2025
Description: Creates a madlib from eight variables.
"""
# creates create_story function
def create_story(person_one, person_two, pet_name, \
                        animal, place, adjective, verb, adverb):
    # creates story variable
    story = (
        person_one + " and " + person_two + " were best friends.\n" +
        "One day " + person_one + " and " + person_two + " decided to go on a\n" +
        "vacation to " + place + ". However, they didn't know\n" +
        "what to do with their " + adjective + " pet " 
        + animal + " named " + pet_name + ".\n" +
        pet_name + " had been causing problems, due to constant " + verb + "ing.\n" +
        person_one + " found a sitter for their pet, and " + 
        adverb + " went on the trip."
    )
    return story

def main():
    person_one = "Joe" 
    person_two = "Lily" 
    pet_name = "Poncho"
    animal = "polar bear"
    place = "Madagascar"
    adjective = "Ridiculous"
    verb = "plank"
    adverb = "spastically"
    # calls back to create story
    story = create_story(person_one, person_two, pet_name, \
                        animal, place, adjective, verb, adverb)
    print(story)
    
main()
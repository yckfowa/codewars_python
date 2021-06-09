geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    for el in geese:
        if el in birds:
            birds.remove(el)
    return birds

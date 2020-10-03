from .models import Deck


def build():
    """
    This function builds the deck model, if it already doesnt exist.
    """
    if not Deck.objects.all():
        for suit in ['Clubs', 'Spades', 'Diamonds', 'Hearts']:
            values = list(range(2,11)) + ["King", "Queen", "Jack", "Ace"]
            for i in values:
                card = Deck(suit=suit, value=i)
                card.save()
                card.set_color_face()
                card.save()

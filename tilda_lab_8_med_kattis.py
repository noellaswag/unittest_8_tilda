from linkedQfilelab8 import LinkedQ


class Syntaxfel(Exception):  # ärver från Exception
    pass  # fungerar som vilket exception som helst, om vi hittar något syntaxfel


def qText(q, ord):
    for b in range(len(ord)):  # första bokstaven högst upp (omvänd inputordning)
        q.enqueue(ord[b])


# Kollar nummer, fick endast vara från 2 och uppåt, alltså ej 0 eller 1
def check_number(q):
    x = q.peek()
    if x == "0":
        q.dequeue()
        raise Syntaxfel("För litet tal vid radslutet")
    if x == "1":
        q.dequeue()
        if q.is_empty():
            raise Syntaxfel("För litet tal vid radslutet")
    while q.is_empty() is False:
        x = q.peek()
        if x.isdigit() is False:  # om x inte är en siffra : raise syntaxfel
            raise Syntaxfel("Bokstav efter siffra vid radslutet")
        q.dequeue()


# kollar om first bokstav är uppercase
def first(q):
    first = q.peek()
    if first.isupper():
        q.dequeue()  # isåfall dequeuea
    else:  # om inte första är uppercase så följer den ej syntaxen
        print(q.dequeue())
        raise Syntaxfel("Saknad stor bokstav vid radslutet")


def next(q):
    next = q.peek()
    if next is not None:  # så länge next har en bokstav efter
        if next.islower():  # kollar om next har liten bokstav
            q.dequeue()
            next = q.peek()
        # har antingen en liten bokstav, då tas den bort av tidigare if-sats, annars har den för många stora/små bokstäver
        if next is not None:  # om next inte är none, kolla om det är en siffra
            if next.isdigit():
                pass  # om det är en siffra låt det pass
            else:
                raise Syntaxfel("Bokstavsfel vid radslutet ")


def atom(q):
    first(q)
    next(q)
    check_number(q)


def try_syntax(q):
    try:
        atom(q)
    except Syntaxfel as syntaxfel:
        return (syntaxfel)
    return "Formeln är syntaktiskt korrekt"




def main():
    ord = ""
    while ord != "#":
        ord = input()
        if ord == "#":
            break
        q = LinkedQ()  # skapar först en kö
        qText(q, ord)
        svar = try_syntax(q)
        # print(svar, end="")

        # alt 2
        #        resultat = try_syntax(ord)
        #        resultat2=try_new_syntax(ord)
        #        print(resultat1)
        #        print(resultat2)

        string_left = ""
        while q.is_empty() is False:
            string_left += q.dequeue()
        if string_left != "":
            print(str(svar) + " " + string_left)
        else:
            print(svar)


if __name__ == '__main__':
    main()
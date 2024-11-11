# Beispiel
test = "Das ist ein Beispielsatz"
print("Text:", test)

# Anzahl Suchtexte
such = "ei"
anz = test.count(such)
print("count: Der String", such, "kommt", anz, "mal vor")

# Erste Position des Suchtextes
anfpos = test.find(such)
print("find 1 'ei': Zum ersten Mal an Position", anfpos)

# Weitere Position des Suchtextes
nextpos = test.find(such, anfpos+1)
print("find 2 'ei': Ein weiteres Mal an Position", nextpos)

# Letzte Position des Suchtextes
endpos = test.rfind(such)
print("rfind 'ei': Zum letzten Mal an Position", endpos)

# Suchtext nicht gefunden
such = "am"
pos = test.find(such)

if pos == -1:
    print("find 'am':", such, "wurde nicht gefunden")
else:
    print("find 'am':", such, "an Position", pos, "gefunden")

# Ersetzen von Text
test = test.replace("ist", "war")
print("replace:", test)

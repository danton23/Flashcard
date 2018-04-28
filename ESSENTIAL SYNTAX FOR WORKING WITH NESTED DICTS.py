vocab= {}
vocab={'dog':{'Hund:dog'}}
vocab={"dog":{"Hund:dog", }, "rabbit":{"peter:brian"}}
print (vocab)
del vocab ['dog']
print (vocab)
vocab= {"dog":{"Hund":"dog","perro":"dog"}, "rabbit":{"peter:brian"}}
del vocab["dog"]["perro"]
print (vocab)


#in dictioanry key and value MUST be individually placed in " "
#e.g "sandwhich":"ham" NOT "sanwhich:ham" otherwise gets confused
#to specify a particular key WITHIN a dictionary we use the syntax
#dictionary [subdic][key] (and can continue in this fashion)

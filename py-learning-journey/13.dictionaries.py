bundle = {
    "Sanjey":45,
    "Alex":7,
    "Vinay":[29,292],
    "Vimal":29,
    "Sanjey":47
}
print(bundle.get("Sanjey"))
print( "Keys are : ",bundle.keys())
print( "Values are : ",bundle.values())

for key,value in bundle.items():
    print(f"{key}:{value}")
bundle.update({"Annoy":45})
print(bundle)

bundle.pop("Vimal")
print(bundle)

print(bundle.get("Vinay")[0])

for num in bundle.get("Vinay"):
    print(num,end=" ")
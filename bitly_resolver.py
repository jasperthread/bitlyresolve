import requests

thegoods = []

# bitlys.txt is a list of shortened urls.
with open('bitlys.txt') as file:
    for line in file:
        try:
            theurl = requests.get(line)
            resolved = theurl.url
			# uncomment for the embedded version
            # resolved = resolved.replace("watch?v=", "embed/")
            print(line.strip(), "-->", resolved)
            thegoods.append(resolved)
        except:
            print('"' + line.strip() + '" is not a valid url.')

with open('output.txt', 'w') as outfile:
    for item in thegoods:
        outfile.write(item + "\n")

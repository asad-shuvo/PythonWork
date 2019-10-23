import io
# Arbitrary String
message = 'This is just a normal string.'

# Use StringIO method to set as file object
f = io.StringIO(message)
print(f.read())
f.write(' Second line written to file like object')

# Reset cursor just like you would a file# Reset
f.seek(0)

# Read again# Read
print(f.read())
# Close the object when contents are no longer needed
f.close()

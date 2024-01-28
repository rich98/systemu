import win32com.client

# Create an instance of the Windows Update Agent object.
wua = win32com.client.Dispatch("Microsoft.Update.Session")

# Create an update searcher object.
searcher = wua.CreateUpdateSearcher()

# Search for installed updates.
search_result = searcher.Search("IsInstalled=1")

# Print details about each installed update.
for i in range(search_result.Updates.Count):
    update = search_result.Updates.Item(i)
    print(f"Update {i + 1}:")
    print(f"  Title: {update.Title}")
    print(f"  Description: {update.Description}")
    print(f"  Installation Date: {update.InstallationBehavior.rebootBehavior}")
    print()

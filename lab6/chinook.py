from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["artists-albums-tracks-database"]

media_types = db["media_types"]
genres=db["genres"]

playlists = {"PlaylistId": "INTEGER", "Name": "NVARCHAR(120)"}
playlist_track = {"PlaylistId": playlists, "TrackId": "INTEGER"}

artists = {"ArtistID": "INTEGER", "Name": "NVARCHAR(120)"}
albums = {"AlbumID": artists, "Title": "NVARCHAR(160)", "ArtistId": "INTEGER"}

employees = {"EmployeeID":"INTEGER", "LastName": "NVARCHAR(20)", "FirstName":"NVARCHAR(20)", "Title": "NVARCHAR(20)"
             , "ReportsTo": "INTEGER", "Birthdate": "DATETIME", "HireDate": "DATETIME", "Address": "NVARCHAR(70)"}
customers = {"CustomerID": employees, "FirstName": "NVARCHAR(40)", "LastName": "NVARCHAR(20)", "Company": "NVARCHAR(80)",
              "Address": "NVARCHAR(70)", "City": "NVARCHAR(40)", "State": "NVARCHAR(40)", "Country": "NVARCHAR(40)", 
             "PostalCode": "NVARCHAR(10)", "Phone": "NVARCHAR(24)", "Fax": "NVARCHAR(24)", "Email": "NVARCHAR(60)", "SupportRepId": "INTEGER"}
invoices = {"InvoiceID": customers, "CustomerId": "INTEGER", "InvoiceDate": "DATETIME", "Billingaddress": "NVARCHAR(24)", "BillingCity": "NVARCHAR(24)"}
invoice_items = {"Invoiceltemld": invoices, "InvoiceID": "INTEGER", "TrackID": "INTEGER", "UnitPrice": "NUMERIC"
                 , "Quantity": "INTEGER"}

TracksID = [playlist_track, albums, invoice_items]
tracks = {"TrackID": TracksID, "Name": "NVARCHAR(200)", 
          "AlbumId":"INTEGER", "MediaTypeID": "INTEGER", "Genreld": "INTEGER", 
          "Composer": "NVARCHAR(220)", "Milliseconds": "INTEGER", "Bytes": "INTEFER",
          "UnitPrice": "NUMERIC"}


media_types.insert_one({"MediaTypeId": tracks, "Name": "NVARCHAR(120)"})
genres.insert_one({"GenreID": tracks, "Name": "NVARCHAR(120)"})
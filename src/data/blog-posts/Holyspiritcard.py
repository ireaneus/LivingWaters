from ace_tools import display_dataframe_to_user
import pandas as pd

# Data for the Holy Spirit Reference Card
data = [
    {
        "Category": "Role",
        "Description": "Convicts the world",
        "Scripture": "John 16:8–11",
        "Full Verse": "And He, when He comes, will convict the world regarding sin, and righteousness, and judgment: regarding sin, because they do not believe in Me; and regarding righteousness, because I am going to the Father and you no longer are going to see Me; and regarding judgment, because the ruler of this world has been judged."
    },
    {
        "Category": "Role",
        "Description": "Teaches and reminds",
        "Scripture": "John 14:26",
        "Full Verse": "But the Helper, the Holy Spirit whom the Father will send in My name, He will teach you all things, and remind you of all that I said to you."
    },
    {
        "Category": "Role",
        "Description": "Guides into truth",
        "Scripture": "John 16:13",
        "Full Verse": "But when He, the Spirit of truth, comes, He will guide you into all the truth; for He will not speak on His own, but whatever He hears, He will speak; and He will disclose to you what is to come."
    },
    {
        "Category": "Role",
        "Description": "Empowers witnessing",
        "Scripture": "Acts 1:8",
        "Full Verse": "But you will receive power when the Holy Spirit has come upon you; and you shall be My witnesses both in Jerusalem, and in all Judea and Samaria, and as far as the remotest part of the earth."
    },
    {
        "Category": "Role",
        "Description": "Sanctifies",
        "Scripture": "Romans 15:16",
        "Full Verse": "To be a minister of Christ Jesus to the Gentiles, ministering as a priest the gospel of God, so that my offering of the Gentiles may become acceptable, sanctified by the Holy Spirit."
    },
    {
        "Category": "Role",
        "Description": "Intercedes for believers",
        "Scripture": "Romans 8:26",
        "Full Verse": "Now in the same way also the Spirit helps our weakness; for we do not know what to pray for as we should, but the Spirit Himself intercedes for us with groanings too deep for words."
    },
    {
        "Category": "Role",
        "Description": "Gives spiritual gifts",
        "Scripture": "1 Corinthians 12:4–11",
        "Full Verse": "Now there are varieties of gifts, but the same Spirit... But one and the same Spirit works all these things, distributing to each one individually just as He wills."
    },
    {
        "Category": "Role",
        "Description": "Assures of adoption",
        "Scripture": "Romans 8:16",
        "Full Verse": "The Spirit Himself testifies with our spirit that we are children of God."
    },
    {
        "Category": "Role",
        "Description": "Seals believers for salvation",
        "Scripture": "Ephesians 1:13–14; 2 Corinthians 1:21–22; 5:5",
        "Full Verse": (
            "Ephesians 1:13–14: In Him, you also, after listening to the message of truth, the gospel of your salvation—"
            "having also believed, you were sealed in Him with the Holy Spirit of the promise, who is a first installment "
            "of our inheritance, in regard to the redemption of God’s own possession, to the praise of His glory.\n"
            "2 Corinthians 1:21–22: Now He who establishes us with you in Christ and anointed us is God, who also sealed us "
            "and gave us the Spirit in our hearts as a pledge.\n"
            "2 Corinthians 5:5: Now He who prepared us for this very purpose is God, who gave us the Spirit as a pledge."
        )
    }
]

df = pd.DataFrame(data)
display_dataframe_to_user(name="Holy Spirit Roles & Verses Card", dataframe=df)

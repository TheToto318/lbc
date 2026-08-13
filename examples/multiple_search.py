"""Search for ads on Leboncoin by location and filters (example: real estate in Paris)."""

import lbc


def main() -> None:
    # Initialize the Leboncoin API client
    client = lbc.Client()

    # Perform a search with various filters
    result = client.search(
        text=["Porsche 924", "Porsche 944"],  # Search for Porsche 924 and Porsche 944
        page=1,
        limit=35,  # Max results per page
        limit_alu=0,  # No auto-suggestions
        sort=lbc.Sort.NEWEST,  # Sort by newest ads
        category=lbc.Category.VEHICULES_VOITURES,  # Car category
        ad_type=lbc.AdType.OFFER,  # Only offers, not searches
        owner_type=lbc.OwnerType.ALL,  # All types of sellers
    )

    # Display summary of each ad
    for ad in result.ads:
        print(f"{ad.id} | {ad.url} | {ad.subject} | {ad.price}€")


if __name__ == "__main__":
    main()

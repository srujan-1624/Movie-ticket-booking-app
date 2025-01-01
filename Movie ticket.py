import sys
import os
import json

movies = {
    1: {"name": "Avengers Endgame", "seats": [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]], "price": 150},
    2: {"name": "Interstellar", "seats": [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]], "price": 180},
    3: {"name": "KGF ch-2", "seats": [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]], "price": 200},
}


def display_movies():
    print("Available Movies:")
    for key, value in movies.items():
        print(f"{key}: {value['name']} - Rs. {value['price']} per ticket")


def choose_movie():
    movie_id = int(input("Enter the movie ID to book tickets: "))
    if movie_id in movies:
        print(f"Selected Movie: {movies[movie_id]['name']}")
        print("Available Seats:")
        for row in movies[movie_id]['seats']:
            print(row)
        return movie_id
    else:
        print("Invalid Movie ID")
        return None


def book_tickets(movie_id):
    if movie_id in movies:
        seats_to_book = int(input("Enter the number of seats to book: "))
        available_seats = movies[movie_id]['seats']
        booked_seats = []
        for _ in range(seats_to_book):
            seat_number = int(input("Enter seat number to book: "))
            seat_found = False
            for row in available_seats:
                if seat_number in row:
                    row.remove(seat_number)
                    booked_seats.append(seat_number)
                    print(f"Seat {seat_number} booked successfully")
                    seat_found = True
                    break
            if not seat_found:
                print(f"Seat {seat_number} is already booked or does not exist")
        generate_bill(movie_id, booked_seats)
    else:
        print("Invalid Movie ID")


def generate_bill(movie_id, booked_seats):
    movie = movies[movie_id]
    total_price = len(booked_seats) * movie["price"]
    print("\n***** Movie Ticket Bill *****")
    print(f"Movie: {movie['name']}")
    print(f"Seats: {booked_seats}")
    print(f"Price per ticket: Rs. {movie['price']}")
    print(f"Total Price: Rs. {total_price}")
    print("****************************\n")


def main():
    while True:
        display_movies()
        movie_id = choose_movie()
        if movie_id:
            book_tickets(movie_id)
        else:
            print("Please select a valid movie.")
        another_booking = input("Do you want to book another ticket? (yes/no): ").lower()
        if another_booking != 'yes':
            break

if __name__ == "__main__":
    main()

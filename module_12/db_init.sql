use testdb;

CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*store*/
INSERT INTO store(locale)
    VALUES('123 Fake St Omaha, NE 68163');

/*books*/
INSERT INTO book(book_name, author)
    VALUES('The Fault in Our Stars', 'John Green');

INSERT INTO book(book_name, author)
    VALUES('The Alchemist', 'Paulo Coelho');

INSERT INTO book(book_name, author, details)
    VALUES('To Kill a Mockingbird', 'Harper Lee', 'We all read it in school');

INSERT INTO book(book_name, author, details)
    VALUES('The Hunger Games', 'Suzanne Collins', 'First in the series');

INSERT INTO book(book_name, author)
    VALUES('The Da Vinci Code', 'Dan Brown');

INSERT INTO book(book_name, author)
    VALUES('The Book Thief', 'Markus Zusak');

INSERT INTO book(book_name, author, details)
    VALUES('Harry Potter and the Sorcerers Stone', 'J.K. Rowling', 'First in the wizard series');

INSERT INTO book(book_name, author)
    VALUES('The Help', 'Kathryn Stockett');

INSERT INTO book(book_name, author, details)
    VALUES('1984', 'George Orwell', 'Famous dystopian novel');

/*users*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Brian', 'Majurinen');

INSERT INTO user(first_name, last_name)
    VALUES('Stephen', 'Lappe');

INSERT INTO user(first_name, last_name)
    VALUES('Homer', 'Simpson');

/*needed help with these*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Brian'), 
        (SELECT book_id FROM book WHERE book_name = '1984')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Stephen'),
        (SELECT book_id FROM book WHERE book_name = 'The Help')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Homer'),
        (SELECT book_id FROM book WHERE book_name = 'The Book Thief')
    );

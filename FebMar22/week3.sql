-- Created Actors
insert into actor (firstName, lastName) values ('Michael J', 'Fox');
insert into actor (firstName, lastName) values ('Christopher', 'Lyoyd');
insert into actor (firstName, lastName) values ('Sylvester', 'Stallone'), ('David', 'Carouso'), ('Brian', 'Denning');
-- Created Movies (minus user for now)
insert into movie (title, year, genre, description) values ('Back to the Future I', 1984, 'Syfy', 'Crazy doc figures out time travel with a delorian'),('Back to the Future II', 1985, 'Syfy', 'Crazy doc figures out time travel with a delorian but goes to the future not past'), ('Rambo 1st Blood', 1982, 'Action', 'Fighting movie');

-- added the right actors to their movie
insert into movie_has_actor (movie_id, actor_id) values(1,1);
insert into movie_has_actor (movie_id, actor_id) values(1,2);
insert into movie_has_actor (movie_id, actor_id) values(3,1), (3, 2), (4,3),(4,4), (4,5);

-- Join statements

-- Viewing 1 actor and their movies
select * from actor left join movie_has_actor on actor.id = movie_has_actor.actor_id right join movie on movie_has_actor.movie_id = movie.id where actor.id = 1;
-- Viewing 1 movies and it's actors
select * from movie left join movie_has_actor on movie.id = movie_has_actor.movie_id left join actor on movie_has_actor.actor_id = actor.id where movie.id = 1;
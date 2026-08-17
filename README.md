# Database Success Broker Failure Inconsistency

This Python script simulates a common problem in distributed systems: a database operation succeeds, but a subsequent message broker operation fails. It demonstrates how this can lead to data inconsistency, where one part of the system (the database) has updated state, but other parts (relying on messages from the broker) are unaware.

## Language

`python`

## How to Run

Save the code as `main.py`.
Run from your terminal: `python main.py`

## Original Article

This example accompanies the Turkish article: [Veritabanı "Başarılı" Dedi, Mesaj Brokerı "Tekrar Dene" Neden? Dağıtık Sistemlerde Tutarlılık Zorlukları](https://fatihsoysal.com/blog/veritabani-basarili-dedi-mesaj-brokeri-tekrar-dene-neden-dagitik-sistemlerde-tutarlilik-zorluklari/).

## License

MIT — see [LICENSE](LICENSE).

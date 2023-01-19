module default {
    type Quote {
        required property text -> str {
            # Loose constraint, may be changed in the future
            constraint max_len_value(200);
        }

        property quotee -> str {
            constraint max_len_value(50);
        }

        property date -> datetime {
            default := datetime_of_statement();
        }
    }
}

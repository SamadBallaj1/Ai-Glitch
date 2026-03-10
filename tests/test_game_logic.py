from logic_utils import check_guess, parse_guess


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_too_high_message_tells_player_to_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_parse_negative_number_edge_case():
    ok, value, error = parse_guess("-5")
    assert ok is True
    assert value == -5
    assert error is None


def test_parse_decimal_number_edge_case():
    ok, value, error = parse_guess("42.9")
    assert ok is True
    assert value == 42
    assert error is None


def test_parse_extremely_large_number_edge_case():
    ok, value, error = parse_guess("999999999999999999999")
    assert ok is True
    assert value > 50
    assert error is None

    outcome, message = check_guess(value, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

from scripts.format_readmes import clean_file


def test_clean_file_reports_missing_path(capsys, tmp_path):
    missing_path = tmp_path / "missing.md"

    assert clean_file(str(missing_path)) is None

    out = capsys.readouterr().out
    assert f"File {missing_path} not found." in out


def test_clean_file_normalizes_basic_english_markdown(tmp_path):
    readme = tmp_path / "README.md"
    readme.write_text(
        "[News & Information](#news-information)\n"
        "Intro\ttext</br>\n"
        "Value\u00A0with trailing spaces   \n",
        encoding="utf-8",
    )

    clean_file(str(readme), is_chinese=False)

    content = readme.read_text(encoding="utf-8")
    assert "[News Information](#news-information)" in content
    assert "Intro text<br>" in content
    assert "Value with trailing spaces" in content
    assert "\t" not in content
    assert "\u00A0" not in content
    assert "trailing spaces   " not in content


def test_clean_file_normalizes_chinese_toc_link(tmp_path):
    readme = tmp_path / "README-CN.md"
    readme.write_text("[GPT/LLMs \u5e94\u7528](#gpt-llms\u5e94\u7528)\n", encoding="utf-8")

    clean_file(str(readme), is_chinese=True)

    assert readme.read_text(encoding="utf-8") == "[GPT-LLMs\u5e94\u7528](#gpt-llms\u5e94\u7528)"


def test_clean_file_removes_blank_lines_inside_table_blocks(tmp_path):
    readme = tmp_path / "README.md"
    readme.write_text(
        "| Name | Description |\n"
        "\n"
        "| Tool A | First row |\n"
        "\n"
        "| Tool B | Second row |\n"
        "\n"
        "Outside table\n",
        encoding="utf-8",
    )

    clean_file(str(readme))

    content = readme.read_text(encoding="utf-8")
    assert "| Name | Description |\n| Tool A | First row |\n| Tool B | Second row |" in content
    assert "| Tool B | Second row |\n\nOutside table" in content


def test_clean_file_keeps_non_table_blank_lines(tmp_path):
    readme = tmp_path / "README.md"
    readme.write_text("Paragraph one\n\nParagraph two\n", encoding="utf-8")

    clean_file(str(readme))

    assert readme.read_text(encoding="utf-8") == "Paragraph one\n\nParagraph two"

# Quantum Many-Body Physics Calculations with Large Language Models

This repository hosts the code and data associated with the paper "Quantum Many-Body Physics Calculations with Large Language Models."

## Installation and Execution

- **Requirement**: `openai` version 0.28.1.
- **Configuration**: Place your OpenAI API key in a `.env` file in the root directory, using the format `OPENAI_API_KEY=your_key_here`.
- **Running the Code**: Navigate to the directory named after the arXiv number of interest and execute `python ../utils.py ../Prompt_template.md {arxiv_number}`, replacing `{arxiv_number}` with the actual arXiv number.

## File Structure

Each arXiv paper is represented by a directory containing:

- `{arxiv_number}.pdf`: The arXiv paper.
- `{arxiv_number}.tex`: LaTeX source for the paper.
- `{arxiv_number}_SM.pdf`: Supplemental material.
- `{arxiv_number}_SM.tex`: LaTeX source for the supplemental material.
- `{arxiv_number}.yaml`: Configuration file with placeholders, extraction, execution results, and scoring details.
- `{arxiv_number}_auto.md`: Execution output.
- `{arxiv_number}_extractor.md`: Extraction output.
- `{arxiv_number}_extractor.ipynb`: Extraction helper functions.
- `{arxiv_number}_execution.ipynb`: Execution helper functions.
- `{arxiv_number}_score_prompt.ipynb`: Scoring and correction helper functions.

### Printouts

Located in `printout`:

- `{arxiv_number}_execution.pdf`: Human-readable execution result.
- `{arxiv_number}_extraction.pdf`: Human-readable extraction result.
- `{arxiv_number}_execution.tex`: LaTeX source for execution result.
- `{arxiv_number}_extraction.tex`: LaTeX source for extraction result.
- `{arxiv_number}_execution.md`: Markdown for execution result.
- `{arxiv_number}_extraction.md`: Markdown for extraction result.

### Additional Resources

- `Rubrics.md`: Scoring rubrics.
- `Naming.yaml`: Mapping of the task names used in `Prompt_template.md` and in the paper for readability.
- `processed_oneshot_df_reverified_scores_renamed.yaml`: Results of one-shot extraction.
- `Prompt_template.md`: Prompt templates.
- `Task_type.yaml`: Task types.

# Authors

Haining Pan, Nayantara Mudur, Will Taranto, Maria Tikhanovskaya, Subhashini Venugopalan, Yasaman Bahri, Michael P. Brenner, Eun-Ah Kim
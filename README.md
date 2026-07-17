```console
$ otel trace --service wassim-badraoui

  EPITA · MSc AI & ML         ████████████████████████████████
  McKay Brothers · Rust, HFT                      ███
  Ministère des Armées · RAG                         ██████
  Devoteam · K8s AIOps                                      ███
                                2022          2024         2026

  wassim badraoui · machine learning engineer · paris
  three roles back to back since 2024. next span opens october 2026.
```

I build ML systems and make them survive production. Lately that means Kubernetes reliability: predicting failures, finding root causes, and proving the model actually works on a real cluster.

I care about whether a result holds up. My repos ship their limitations next to their numbers.

## Reliability & AIOps

| Repo | What it is |
|---|---|
| [otel-sre-copilot](https://github.com/Wassbdr/otel-sre-copilot) | LangGraph agent that investigates Kubernetes incidents through OpenTelemetry (Prometheus, Tempo, Loki). Ships with a reproducible eval harness against 3 baselines, with Chaos Mesh as ground truth. The full benchmark run is still pending. |
| [matrix_simple](https://github.com/Wassbdr/matrix_simple) | STA, spatio-temporal GNN for microservice root cause analysis. Selects k suspect nodes first, which drops the cost from O(N²) to O(N+k²). Latency stays flat as the graph grows. |
| [ewat](https://github.com/Wassbdr/ewat) | Early warning and anomaly typing on K8s microservices. Separates benign drift from real anomalies, then learns a fault ontology. Validated on a live 9-node cluster. |
| [slcmca](https://github.com/Wassbdr/slcmca) | slacheck. Answers "what SLA can I actually commit to?" for a multi-cloud microservice app, by walking the Datadog APM call graph and finding the critical path. Catches SLOs you promised but cannot hit. |
| [mlops2](https://github.com/Wassbdr/mlops2) | End-to-end MLOps pipeline: scikit-learn to FastAPI to Docker to a VM, deployed by GitHub Actions. |

## LLM & agents

| Repo | What it is |
|---|---|
| [memento](https://github.com/Wassbdr/memento) | Voice-first memory assistant for Alzheimer patients. RAG plus a knowledge graph, no buttons and no screen, because the interface is the part patients cannot use. |
| [voicecall](https://github.com/Wassbdr/voicecall) | Voice agent that runs entirely on your machine: faster-whisper, a local Ollama model, Edge TTS, OpenVoice cloning. No API call ever leaves the box. |
| [arcad](https://github.com/Wassbdr/arcad) | PREDI-Care, multi-agent clinical decision support for rectal cancer strategy. Built at the A.R.CA.D hackathon. |

## Systems & fundamentals

| Repo | What it is |
|---|---|
| [sklearn2c](https://github.com/Wassbdr/sklearn2c) | Transpiles a trained scikit-learn model into dependency-free C, so it runs on an Arduino or an STM32. |
| [abs_arg_dung](https://github.com/Wassbdr/abs_arg_dung) | Dung's abstract argumentation framework, all 7 semantics. Symbolic AI: given who attacks whom, graph theory decides which arguments survive. |
| [prog_diff](https://github.com/Wassbdr/prog_diff) | An autodiff engine written from scratch in NumPy, up to Conv2d, BatchNorm and Adam. The way to learn what PyTorch does is to rebuild it. |
| [ct_visualizer](https://github.com/Wassbdr/ct_visualizer) | 2D/3D CT viewer with segmentation overlays, built as a data-quality tool for the PINKCC ovarian cancer challenge, where our team finished 7th of 42. |

## Elsewhere

Contributor to open source AI infrastructure: a merged PR in [litellm](https://github.com/BerriAI/litellm), plus work on [dspy](https://github.com/stanfordnlp/dspy) and [opentelemetry-rust](https://github.com/open-telemetry/opentelemetry-rust).

Also worth a look: a CUDA inference engine written from scratch that beats PyTorch on CNNs by roughly 4x, a 42sh POSIX shell in C, and research on whether a backdoor can survive knowledge distillation into a clean student model. Some of that lives in team or school repos.

## Contact

Looking for a first full-time ML engineering role in Paris, starting October 2026.

[LinkedIn](https://www.linkedin.com/in/wassim-badraoui) · [wassim.badraoui@epita.fr](mailto:wassim.badraoui@epita.fr)

# Unified Business Card Application

## Introduction

This repository contains the implementation of some conveniant approach to the business card exchange. This concept arises from the irregular distribution of physical business cards due to organizational changes and varying card usage based on occupation. Aiming to provide a more flexible, convenient, and lightweight alternative, we propose a mobile business card exchange system using QR codes, which are readily recognizable by any smartphone's camera.

## Objective

This project starts with a proof of concept (PoC) in Python. Following that, we plan to write modules in Rust, which could be called from different languages. Our primary targets are Python for module verification and Flutter for actual usage. Advanced features plan to include Flutter swipe actions, multiple business card options, and more.

## Core Functionality

The system transforms contact information into [the vCard standard](https://datatracker.ietf.org/doc/html/rfc6350) and facilitates the creation or scanning of [QR codes](https://www.qrcode.com/en/about/standards.html).

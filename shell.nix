{pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {

    packages = [
      (pkgs.python3Full.withPackages(pypkgs: [pypkgs.pygame]))
    ];
}

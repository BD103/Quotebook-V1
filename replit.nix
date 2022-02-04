{ pkgs }: {
    deps = [
        pkgs.python39Full
        pkgs.poetry
        pkgs.nodePackages.prettier
        pkgs.vim
    ];
}

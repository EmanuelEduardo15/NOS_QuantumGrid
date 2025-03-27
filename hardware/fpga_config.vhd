library IEEE;
entity CurvatureAccelerator is
    Port ( clk : in STD_LOGIC;
           curvature_in : in STD_LOGIC_VECTOR(15 downto 0));
end CurvatureAccelerator;

architecture Behavioral of CurvatureAccelerator is
begin
    process(clk)
    begin
        if rising_edge(clk) then
            -- Implementação HCT aqui
        end if;
    end process;
end Behavioral;

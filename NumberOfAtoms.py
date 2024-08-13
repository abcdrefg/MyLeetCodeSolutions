class Solution:

    def sum_dictionaries(self, atoms, atoms2):
        for key, value in atoms.items():
            if key not in atoms2:
                atoms2[key] = value
                continue
            atoms2[key] += value
        return atoms2

    def get_number(self, substring, index_to_return):
        number = ''
        if not substring:
            return 1, index_to_return + 1
        for s in substring:
            if s.isdigit():
                index_to_return += 1
                number += s
            else:
                if not number:
                    number = 1
                return int(number), index_to_return + 1
        return int(number), index_to_return + 1



    def calculate_multiplier(self, subformula, multiplier):
        sub_size = len(subformula)
        atoms = {}
        i = 0
        current_digit = ''
        current_atom = ''
        while i < sub_size:
            if subformula[i] == '(':
                if current_atom:
                    if current_atom not in atoms:
                        atoms[current_atom] = 1
                    else:
                        atoms[current_atom] += 1
                current_digit = ''
                current_atom = ''
                beginning = i
                counter_of_openings = 1
                closure_idx = 0
                while True:
                    i += 1
                    if subformula[i] == '(':
                        counter_of_openings += 1
                        continue
                    if subformula[i] == ')':
                        if counter_of_openings == 1:
                            closure_idx = i
                            break
                        counter_of_openings -= 1
                        continue
                temp_multiplier, final_index = self.get_number(subformula[closure_idx + 1:], closure_idx)
                atoms = self.sum_dictionaries(atoms, self.calculate_multiplier(subformula[beginning + 1:closure_idx], temp_multiplier))
                i = final_index
                continue

            if subformula[i].isdigit() and (i + 1) < sub_size and subformula[i + 1].isdigit():
                current_digit += subformula[i]
                i += 1
                continue
            if subformula[i].isdigit():
                current_digit += subformula[i]
                if current_atom not in atoms:
                    atoms[current_atom] = 0
                atoms[current_atom] += int(current_digit)
                current_atom = ''
                current_digit = ''
                i += 1
                continue
            if subformula[i].islower():
                current_atom += subformula[i]
            else:
                if current_atom:
                    if current_atom not in atoms:
                        atoms[current_atom] = 1
                    else:
                        atoms[current_atom] += 1
                current_atom = subformula[i]
            i += 1

        if current_atom:
            if current_atom not in atoms:
                atoms[current_atom] = 1
            else:
                atoms[current_atom] += 1

        for key, value in atoms.items():
            atoms[key] = value*multiplier
        return atoms

    def countOfAtoms(self, formula: str) -> str:
        atoms = self.calculate_multiplier(formula, 1)
        final_s = ''
        for key, value in sorted(atoms.items()):
            final_s += key
            if value > 1:
                final_s += str(value)
        return final_s

Solution().countOfAtoms("Mg(H2O)")

